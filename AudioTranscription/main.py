from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import openai
from transformers import pipeline
from pydub import AudioSegment
import tempfile
import asyncio
import os

# Initialize FastAPI app
app = FastAPI()

# Load models
openai.api_key = "sk-proj-kFlYkOMDsuiyjAUQgi7rT3BlbkFJy44n1WZYUwOtz3RODB7t"
summarizer = pipeline("summarization")

# Define a request model
class TranscriptionResult(BaseModel):
    transcription: str
    summary: str
    timestamps: list

async def save_temp_file(file: UploadFile):
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, file.filename)
    with open(temp_path, 'wb') as temp_file:
        content = await file.read()
        temp_file.write(content)
    return temp_path

async def transcribe_audio(file_path: str):
    # Load and convert the audio file to a format suitable for Whisper
    audio = AudioSegment.from_file(file_path)
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio.export(temp_wav.name, format="wav")

    # Transcribe audio using OpenAI's Whisper model
    with open(temp_wav.name, 'rb') as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    
    # Clean up temporary files
    os.remove(temp_wav.name)
    return response['text'], response['segments']

def extract_timestamps(segments):
    timestamps = []
    for segment in segments:
        timestamps.append({
            "start": segment['start'],
            "end": segment['end'],
            "text": segment['text']
        })
    return timestamps

@app.post("/transcribe", response_model=TranscriptionResult)
async def transcribe(file: UploadFile = File(...)):
    # Save the uploaded file to a temporary location
    file_path = await save_temp_file(file)

    # Transcribe the audio file
    transcription, segments = await transcribe_audio(filepath)

    # Summarize the transcription
    summary = summarizer(transcription, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

    # Extract timestamps
    timestamps = extract_timestamps(segments)

    # Clean up the temporary file
    os.remove(file_path)

    return TranscriptionResult(
        transcription=transcription,
        summary=summary,
        timestamps=timestamps
    )

    # Save results to a JSON file

    
    # result_file = "transcription_result.json"
    # with open(result_file, 'w') as f:
    #     json.dump(result.dict(), f)

    # return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
