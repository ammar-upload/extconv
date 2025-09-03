import React, { useEffect, useMemo, useRef, useState } from "react";
import JSZip from "jszip";
import { saveAs } from "file-saver";
import {
  Upload,
  Download,
  FileType,
  File,
  Music,
  Image,
  Video,
  FileText,
  X,
  Sun,
  Moon,
  Search,
} from "lucide-react";

const EXTENSIONS = [
  "pdf","doc","docx","odt","rtf","txt","xls","xlsx","ods","ppt","pptx","odp",
  "csv","tsv","epub","mobi","jpg","jpeg","png","gif","bmp","tiff","tif","svg","webp","heic","ico","raw",
  "mp3","wav","aac","ogg","oga","flac","alac","m4a","aiff","wma","mp4","mkv","mov","avi","wmv","flv",
  "webm","3gp","mpeg","mpg","m4v","html","css","js","jsx","ts","tsx","json","xml","yml","yaml","sql",
  "c","cpp","h","hpp","java","py","php","rb","go","rs","kt","swift","sh","bat","pl",
  "zip","rar","7z","tar","gz","bz2","xz","iso","dmg","apk","exe","msi","bin","db","sqlite","mdb","accdb",
  "bak","ini","cfg","log","env","psd","ai","xd","fig","sketch","indd","torrent","ics","vcf",
];

const THEME_KEY = "extconv-theme";

export default function App() {
  const [dark, setDark] = useState(true);
  useEffect(() => {
    const saved = localStorage.getItem(THEME_KEY);
    setDark(saved === "light" ? false : true);
  }, []);
  useEffect(() => {
    localStorage.setItem(THEME_KEY, dark ? "dark" : "light");
    document.body.className = dark
      ? "bg-gradient-to-br from-gray-950 via-gray-900 to-black text-white"
      : "bg-gradient-to-br from-gray-50 via-gray-100 to-gray-200 text-gray-900";
  }, [dark]);

  const [files, setFiles] = useState([]);
  const [dragging, setDragging] = useState(false);
  const [search, setSearch] = useState("");
  const [selectedExt, setSelectedExt] = useState("");
  const fileInputRef = useRef(null);

  const filteredExts = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return [];
    return EXTENSIONS.filter((ext) => ext.includes(q)).slice(0, 15);
  }, [search]);

  const addFiles = (list) => {
    const incoming = Array.from(list || []);
    if (!incoming.length) return;
    setFiles((prev) => [...prev, ...incoming]);
  };

  const convert = async () => {
    if (!selectedExt || files.length === 0) return;

    if (files.length === 1) {
      const file = files[0];
      const newName = file.name.replace(/\.[^/.]+$/, "") + "." + selectedExt;
      const data = await file.arrayBuffer();
      saveAs(new Blob([data], { type: file.type || "application/octet-stream" }), newName);
      return;
    }

    const zip = new JSZip();
    for (const f of files) {
      const base = f.name.replace(/\.[^/.]+$/, "");
      const data = await f.arrayBuffer();
      zip.file(`${base}.${selectedExt}`, data);
    }
    const blob = await zip.generateAsync({ type: "blob" });
    saveAs(blob, "renamed_files.zip");
  };

  const fileIcon = (name) => {
    const ext = name.split(".").pop()?.toLowerCase();
    if (["jpg","jpeg","png","gif","bmp","tiff","tif","svg","webp","heic","ico"].includes(ext))
      return <Image className="w-6 h-6 text-pink-400" />;
    if (["mp3","wav","aac","ogg","oga","flac","alac","m4a","aiff","wma"].includes(ext))
      return <Music className="w-6 h-6 text-green-400" />;
    if (["mp4","mkv","mov","avi","wmv","flv","webm","3gp","mpeg","mpg","m4v"].includes(ext))
      return <Video className="w-6 h-6 text-purple-400" />;
    if (["pdf","doc","docx","txt","xls","xlsx","ppt","pptx","csv"].includes(ext))
      return <FileText className="w-6 h-6 text-blue-400" />;
    return <File className="w-6 h-6 text-gray-400" />;
  };

  return (
    <div className="w-screen h-screen flex flex-col">
      {/* Header */}
      <header className={`w-full px-6 py-4 border-b flex items-center justify-between 
        ${dark ? "border-gray-800 bg-gradient-to-r from-indigo-900 via-purple-900 to-black" 
               : "border-gray-200 bg-gradient-to-r from-blue-50 via-white to-blue-100"} backdrop-blur-md`}>
        <div className="flex items-center gap-2">
          <FileType className={`w-8 h-8 ${dark ? "text-indigo-400" : "text-blue-600"}`} />
          <h1 className="text-2xl font-extrabold bg-gradient-to-r from-indigo-400 to-pink-400 bg-clip-text text-transparent">
            EXTCONV
          </h1>
        </div>
        <button
          onClick={() => setDark((d) => !d)}
          className={`p-2 rounded-full transition hover:scale-110 ${dark ? "bg-gray-800 text-yellow-300" : "bg-gray-100 text-gray-700"}`}
        >
          {dark ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
        </button>
      </header>

      {/* Main */}
      <main className="flex-1 overflow-y-auto flex flex-col items-center px-6 py-8 gap-6">
        {/* Step 1 - Upload */}
        <div
          className={`w-full max-w-4xl rounded-2xl border-2 border-dashed p-10 text-center cursor-pointer transition 
            ${dark ? (dragging ? "border-indigo-400 bg-gray-800/70" : "border-gray-700 bg-gray-900/60 hover:bg-gray-800")
                   : (dragging ? "border-blue-500 bg-blue-50" : "border-gray-300 bg-white hover:bg-gray-50")}`}
          onClick={() => fileInputRef.current?.click()}
          onDrop={(e)=>{e.preventDefault();setDragging(false);addFiles(e.dataTransfer.files);}}
          onDragOver={(e)=>{e.preventDefault();setDragging(true);}}
          onDragLeave={()=>setDragging(false)}
        >
          <Upload className={`w-12 h-12 mx-auto mb-4 ${dark ? "text-indigo-400" : "text-blue-600"}`} />
          <p className="font-semibold">Step 1: Upload files</p>
          <p className="text-sm opacity-70">Drag & drop or click to browse</p>
          <input ref={fileInputRef} type="file" multiple className="hidden" onChange={(e)=>addFiles(e.target.files)} />
        </div>

        {/* Step 2 - Select Extension */}
        {files.length > 0 && (
          <div className={`w-full max-w-4xl rounded-xl p-6 shadow-xl 
            ${dark ? "bg-gray-900 border border-gray-800" : "bg-white border border-gray-200"}`}>
            <h2 className="text-lg font-semibold mb-4">Step 2: Choose extension</h2>
            <div className="relative mb-4">
              <div className={`flex items-center gap-2 rounded-lg px-4 py-3 border 
                ${dark ? "bg-gray-800 border-gray-700" : "bg-gray-100 border-gray-300"}`}>
                <Search className="w-5 h-5 opacity-70" />
                <input
                  type="text"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  placeholder="Search extension (e.g. pdf, mp3, png)…"
                  className="flex-1 bg-transparent outline-none"
                />
                {selectedExt && (
                  <span className="text-sm px-2 py-1 rounded bg-indigo-600 text-white">.{selectedExt}</span>
                )}
              </div>
              {search && (
                <div className={`absolute left-0 right-0 mt-1 rounded-lg shadow-xl max-h-64 overflow-y-auto z-10 border 
                  ${dark ? "bg-gray-900 border-gray-700" : "bg-white border-gray-200"}`}>
                  {filteredExts.length > 0 ? (
                    filteredExts.map((ext) => (
                      <button key={ext} onClick={()=>{setSelectedExt(ext);setSearch("");}}
                        className={`w-full text-left px-4 py-2 flex items-center gap-2 transition
                          ${dark ? "hover:bg-gray-800" : "hover:bg-gray-100"} 
                          ${selectedExt===ext ? "bg-indigo-600 text-white" : ""}`}>
                        .{ext}
                      </button>
                    ))
                  ) : (
                    <div className="px-4 py-3 opacity-70">No results</div>
                  )}
                </div>
              )}
            </div>

            {/* File list */}
            <h3 className="text-md font-semibold mb-2">Files Selected</h3>
            <ul className="space-y-2 max-h-60 overflow-y-auto custom-scroll">
              {files.map((file,i)=>(
                <li key={i} className={`flex items-center justify-between p-3 rounded-lg ${dark?"hover:bg-gray-800":"hover:bg-gray-100"}`}>
                  <div className="flex items-center gap-3 truncate">
                    {fileIcon(file.name)}
                    <span className="truncate">{file.name}</span>
                  </div>
                  <button onClick={()=>setFiles(files.filter((_,x)=>x!==i))} className="text-red-500 hover:text-red-600">
                    <X className="w-5 h-5"/>
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}
      </main>

      {/* Step 3 - Convert (sticky footer) */}
      {files.length > 0 && (
        <footer className="w-full p-4 border-t backdrop-blur-md sticky bottom-0 
          bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 flex justify-center">
          <button
            onClick={convert}
            disabled={!selectedExt}
            className={`w-full max-w-md flex items-center justify-center gap-2 rounded-xl py-3 font-bold transition-all duration-300 
              ${!selectedExt 
                ? "bg-gray-500 cursor-not-allowed text-white" 
                : "bg-gradient-to-r from-green-400 to-blue-500 hover:from-blue-500 hover:to-green-400 hover:scale-105 shadow-lg text-white"}`}
          >
            <Download className="w-5 h-5"/>
            Convert & Download
          </button>
        </footer>
      )}

      {/* Custom Scrollbar */}
      <style>{`
  /* Global Custom Scrollbar */
  ::-webkit-scrollbar {
    width: 10px;
    height: 10px;
  }
  ::-webkit-scrollbar-thumb {
    background: linear-gradient(to bottom, #6366f1, #ec4899);
    border-radius: 10px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(to bottom, #4f46e5, #db2777);
  }
  ::-webkit-scrollbar-track {
    background: ${dark ? "#111827" : "#f3f4f6"};
  }
`}</style>

    </div>
  );
}
