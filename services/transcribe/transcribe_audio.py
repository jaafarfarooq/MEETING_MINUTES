import whisper

def transcribe_audio(file_path):
    try:
        # Load the Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio file
        result = model.transcribe(file_path)
        return result["text"]

    except Exception as e:
        print(f"An error occurred: {e}")