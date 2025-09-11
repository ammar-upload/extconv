# backend/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from docx import Document
from pathlib import Path
import logging

# Import your mapping
from inpage_map import inpage_to_unicode

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directories
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# FastAPI app
app = FastAPI(
    title="InPage to DOCX Converter",
    description="Convert InPage (.inp / .txt) files to DOCX format",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


# --- Helper functions ---
def inpage_to_text(content: str) -> str:
    """Convert InPage content to Unicode text using mapping."""
    return "".join(inpage_to_unicode.get(ch, ch) for ch in content)


def clean_text(text: str) -> str:
    """Remove null bytes and unsafe control characters."""
    return "".join(
        ch for ch in text if (ch.isprintable() or ch in "\n\t")
    ).replace("\x00", "")


# --- Routes ---
@app.get("/")
async def root():
    return {"status": "ok", "message": "InPage Converter API is running"}


@app.post("/convert")
async def convert_file(file: UploadFile = File(...)):
    """Convert uploaded InPage/TXT file to DOCX."""
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No filename provided")

        ext = Path(file.filename).suffix.lower()
        if ext not in [".inp", ".txt"]:
            raise HTTPException(
                status_code=400,
                detail="Only .INP and .TXT files are supported"
            )

        # Save uploaded file
        file_path = UPLOAD_DIR / file.filename
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)

        text_content = ""

        if ext == ".txt":
            # Unicode export from InPage
            text_content = content.decode("utf-8", errors="ignore")
            logger.info("Loaded .txt file as UTF-8")
        else:
            # Raw .inp (binary file)
            text_content = content.decode("latin-1", errors="ignore")
            logger.warning("Loaded raw .inp file (may be garbage)")

        # Apply mapping
        converted = inpage_to_text(text_content)

        # Clean unsafe chars
        safe_text = clean_text(converted)

        if not safe_text.strip():
            safe_text = "⚠️ No readable content found. Please export your InPage file as Unicode Text (.txt)."

        # Create Word doc (without heading)
        doc = Document()
        for line in safe_text.splitlines():
            if line.strip():
                doc.add_paragraph(line.strip())

        # Save output
        output_file = OUTPUT_DIR / (Path(file.filename).stem + "_converted.docx")
        doc.save(output_file)

        return FileResponse(
            output_file,
            filename=output_file.name,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# --- Run server ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
