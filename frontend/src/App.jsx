import React, { useEffect, useRef, useState } from "react";
import { Upload, Download, FileType, File, X, AlertCircle } from "lucide-react";

export default function App() {
  const [dark, setDark] = useState(true);
  const [files, setFiles] = useState([]);
  const [dragging, setDragging] = useState(false);
  const fileInputRef = useRef(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [serverStatus, setServerStatus] = useState("checking");

  // ✅ Check server on mount
  useEffect(() => {
    checkServerStatus();
  }, []);

  const checkServerStatus = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/");
      if (response.ok) {
        setServerStatus("online");
        setError("");
      } else throw new Error("Server error");
    } catch {
      setServerStatus("offline");
      setError("⚠️ Backend server is not running. Start FastAPI on port 8000.");
    }
  };

  const addFiles = (list) => {
    const incoming = Array.from(list || []);
    const validFiles = incoming.filter((f) =>
      [".inp", ".inpage"].some((ext) => f.name.toLowerCase().endsWith(ext))
    );

    if (!validFiles.length) {
      setError("❌ Only .INP and .INPAGE files are supported.");
      setTimeout(() => setError(""), 3000);
      return;
    }

    setFiles((prev) => [...prev, ...validFiles]);
  };

  const convert = async () => {
    if (!files.length) return;
    setLoading(true);
    setError("");

    for (const file of files) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const res = await fetch("http://127.0.0.1:8000/convert", {
          method: "POST",
          body: formData,
        });

        if (!res.ok) throw new Error(`Server error: ${res.status}`);

        const blob = await res.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = file.name.replace(/\.(inp|inpage)$/i, "") + "_converted.docx";
        a.click();
        window.URL.revokeObjectURL(url);
      } catch (err) {
        setError(`❌ Failed to convert ${file.name}: ${err.message}`);
      }
    }

    setLoading(false);
  };

  const removeFile = (index) => {
    setFiles(files.filter((_, i) => i !== index));
  };

  const fileIcon = (name) => {
    const ext = name.split(".").pop()?.toLowerCase();
    return ["doc", "docx", "txt", "inp", "inpage"].includes(ext) ? (
      <FileType className="w-6 h-6 text-blue-500" />
    ) : (
      <File className="w-6 h-6 text-gray-400" />
    );
  };

  return (
    <div className={`w-screen h-screen flex flex-col ${dark ? "bg-gray-950 text-gray-100" : "bg-gray-50 text-gray-900"}`}>
      {/* 🔹 Header */}
      <header
        className={`px-6 py-4 border-b flex justify-between items-center shadow-md transition-colors ${
          dark ? "bg-gradient-to-r from-indigo-900 to-purple-900 border-gray-800" : "bg-gradient-to-r from-blue-100 to-blue-50 border-gray-200"
        }`}
      >
        <div className="flex items-center gap-2">
          <FileType className={`w-8 h-8 ${dark ? "text-indigo-400" : "text-blue-600"}`} />
          <h1 className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-pink-400 bg-clip-text text-transparent">
            InPage → DOCX Converter
          </h1>
        </div>
        <div className="flex items-center gap-3">
          <span
            className={`flex items-center gap-2 text-sm px-3 py-1 rounded-full ${
              serverStatus === "online"
                ? "bg-green-600 text-white"
                : serverStatus === "offline"
                ? "bg-red-600 text-white"
                : "bg-yellow-400 text-black"
            }`}
          >
            {serverStatus === "online" ? "🟢 Online" : serverStatus === "offline" ? "🔴 Offline" : "🟡 Checking..."}
          </span>
          <button
            onClick={() => setDark((d) => !d)}
            className={`p-2 rounded-full transition hover:scale-110 ${
              dark ? "bg-gray-800 text-yellow-300" : "bg-gray-200 text-gray-800"
            }`}
          >
            {dark ? "🌞" : "🌙"}
          </button>
        </div>
      </header>

      {/* 🔹 Main */}
      <main className="flex-1 overflow-y-auto flex flex-col items-center px-6 py-8 gap-6">
        {error && (
          <div
            className={`w-full max-w-3xl p-4 rounded-lg border flex items-center gap-2 ${
              dark ? "bg-red-900/30 border-red-600 text-red-300" : "bg-red-100 border-red-500 text-red-700"
            }`}
          >
            <AlertCircle className="w-5 h-5" />
            <p>{error}</p>
          </div>
        )}

        {/* File upload box */}
        <div
          className={`w-full max-w-3xl rounded-2xl border-2 border-dashed p-10 text-center transition cursor-pointer ${
            dark
              ? dragging
                ? "border-indigo-400 bg-gray-800"
                : "border-gray-700 bg-gray-900 hover:bg-gray-800"
              : dragging
              ? "border-blue-500 bg-blue-100"
              : "border-gray-400 bg-white hover:bg-gray-100"
          } ${serverStatus === "offline" ? "opacity-50 cursor-not-allowed" : ""}`}
          onClick={() => serverStatus === "online" && fileInputRef.current?.click()}
          onDrop={(e) => {
            e.preventDefault();
            setDragging(false);
            if (serverStatus === "online") addFiles(e.dataTransfer.files);
          }}
          onDragOver={(e) => {
            e.preventDefault();
            if (serverStatus === "online") setDragging(true);
          }}
          onDragLeave={() => setDragging(false)}
        >
          <Upload className={`w-12 h-12 mx-auto mb-3 ${dark ? "text-indigo-400" : "text-blue-600"}`} />
          <p className="font-semibold">Step 1: Upload .INP / .INPAGE files</p>
          <p className="text-sm opacity-70">
            {serverStatus === "offline" ? "Start backend server first" : "Drag & drop or click to browse"}
          </p>
          <input ref={fileInputRef} type="file" accept=".inp,.inpage" multiple className="hidden" onChange={(e) => addFiles(e.target.files)} />
        </div>

        {/* File list */}
        {files.length > 0 && (
          <div className="w-full max-w-3xl space-y-2">
            {files.map((file, i) => (
              <div
                key={i}
                className={`flex justify-between items-center p-3 rounded-lg border transition ${
                  dark ? "bg-gray-800 border-gray-700" : "bg-white border-gray-300"
                }`}
              >
                <div className="flex items-center gap-3 truncate">
                  {fileIcon(file.name)}
                  <span className="truncate">{file.name}</span>
                  <span className="text-xs opacity-70">({(file.size / 1024).toFixed(1)} KB)</span>
                </div>
                <button onClick={() => removeFile(i)} className="text-red-500 hover:text-red-600">
                  <X className="w-5 h-5" />
                </button>
              </div>
            ))}
          </div>
        )}
      </main>

      {/* 🔹 Footer */}
      {files.length > 0 && serverStatus === "online" && (
       <footer className="sticky bottom-0 w-full p-4 bg-gradient-to-r from-green-500 to-blue-500">
  <button
    onClick={convert}
    disabled={loading}
    className={`w-full max-w-md mx-auto flex justify-center items-center gap-2 py-3 px-6 font-semibold rounded-xl text-white shadow-lg transition-all duration-300 transform
      ${
        loading
          ? "bg-gray-500 cursor-not-allowed"
          : "bg-gradient-to-r from-green-500 to-blue-500 hover:from-blue-500 hover:to-purple-600 hover:shadow-xl hover:scale-105"
      }`}
  >
    <Download className="w-5 h-5" />
    {loading ? "Converting..." : `Convert & Download (${files.length})`}
  </button>
</footer>

      )}
    </div>
  );
}
