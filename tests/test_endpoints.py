import unittest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, MagicMock
import io

client = TestClient(app)

class TestEndpoints(unittest.TestCase):

    @patch("services.transcribe.transcribe_video.transcribe_video")
    @patch("services.chatgpt_response.get_chatgpt_response")
    def test_upload_video(self, mock_get_chatgpt_response, mock_transcribe_video):
        # Mock the transcriptions and ChatGPT response
        mock_transcribe_video.return_value = "This is a video transcript."
        mock_get_chatgpt_response.return_value = "This is a summary of the meeting."

        # Create an in-memory file to act as an uploaded video
        video_file = io.BytesIO(b"fake video content")
        video_file.name = "test.mp4"

        # Send request to /upload/video
        response = client.post("/upload/video", files={"video": ("test.mp4", video_file, "video/mp4")})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a summary of the meeting.", response.json())

    @patch("services.transcribe.transcribe_audio.transcribe_audio")
    @patch("services.chatgpt_response.get_chatgpt_response")
    def test_upload_audio(self, mock_get_chatgpt_response, mock_transcribe_audio):
        # Mock the transcriptions and ChatGPT response
        mock_transcribe_audio.return_value = "This is an audio transcript."
        mock_get_chatgpt_response.return_value = "This is a summary of the audio."

        # Create an in-memory file to act as an uploaded audio file
        audio_file = io.BytesIO(b"fake audio content")
        audio_file.name = "test.wav"

        # Send request to /upload/audio
        response = client.post("/upload/audio", files={"audio": ("test.wav", audio_file, "audio/wav")})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a summary of the audio.", response.json())

    @patch("services.chatgpt_response.get_chatgpt_response")
    def test_upload_transcript(self, mock_get_chatgpt_response):
        # Mock the ChatGPT response
        mock_get_chatgpt_response.return_value = "This is a summary of the transcript."

        # Define the request payload
        payload = {"transcript": "This is the meeting transcript."}

        # Send request to /upload/transcript
        response = client.post("/upload/transcript", json=payload)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a summary of the transcript.", response.json())

if __name__ == "__main__":
    unittest.main()
