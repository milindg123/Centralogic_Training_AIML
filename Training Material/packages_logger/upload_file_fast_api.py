from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import uvicorn

app = FastAPI()

# Directory to store the uploaded PDFs
UPLOAD_DIR = "uploaded_pdfs"

# Create the directory if it doesn't exist
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    # Define the file path
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save the uploaded PDF file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    return JSONResponse(content={"message": "File uploaded successfully", "filename": file.filename})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
