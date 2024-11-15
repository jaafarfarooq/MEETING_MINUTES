import moviepy.editor as mp
import speech_recognition as sr
from services.transcribe.transcribe_audio import transcribe_audio

def transcribe_video(file_path):
    # Load the video 
    video = mp.VideoFileClip(file_path) 
  
    # Extract the audio from the video 
    audio_file = video.audio 
    audio_file.write_audiofile(file_path+".wav")
    text = transcribe_audio(file_path+".wav")
    video.close()
    return text