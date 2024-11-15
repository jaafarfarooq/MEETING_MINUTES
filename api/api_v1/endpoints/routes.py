from fastapi import APIRouter, File, UploadFile
from services.transcribe.transcribe_video import transcribe_video
from services.transcribe.transcribe_audio import transcribe_audio
from services.chatgpt_response.get_chatgpt_response import get_chatgpt_response
from schemas.transcript import TranscriptInput
import os

temp_file_path = "temp"

router = APIRouter()

@router.post("/upload/video")
async def upload_video(video: UploadFile = File(...)):
    response = ""
    try:
        # Write the uploaded video content to temp.mp4
        with open(temp_file_path+'.mp4', "wb") as temp_file:
            temp_file.write(await video.read())
        transcript = transcribe_video(temp_file_path+'.mp4')
        response = get_chatgpt_response(transcript)

    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up the temp.mp4 file after processing
        if os.path.exists(temp_file_path+'.mp4'):
            os.remove(temp_file_path+'.mp4')

    return {response}

@router.post("/upload/audio")
async def upload_audio(audio: UploadFile = File(...)):
    response = ""
    try:
        # Write the uploaded video content to temp.mp4
        with open(temp_file_path+'.wav', "wb") as temp_file:
            temp_file.write(await audio.read())
        transcript = transcribe_audio(temp_file_path+'.wav')
        response = get_chatgpt_response(transcript)

    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up the temp.mp4 file after processing
        if os.path.exists(temp_file_path+'.wav'):
            os.remove(temp_file_path+'.wav')

    return {response}

@router.post("/upload/transcript")
async def upload_transcript(data: TranscriptInput):
    # Read file contents (just for demonstration; we won't save or process it here)
    content = data.transcript
    response =  get_chatgpt_response(content)
    return {response}