import unittest
from unittest.mock import patch, MagicMock
from services.transcribe.transcribe_audio import transcribe_audio

class TestTranscribeAudio(unittest.TestCase):

    @patch("whisper.load_model")
    def test_transcribe_audio_success(self, mock_load_model):
        # Mock the Whisper model and transcribe method
        mock_model = MagicMock()
        mock_load_model.return_value = mock_model
        mock_model.transcribe.return_value = {"text": "This is a test transcription."}

        # Call the function
        result = transcribe_audio("test_audio.wav")

        # Assertions
        mock_load_model.assert_called_once_with("base")
        mock_model.transcribe.assert_called_once_with("test_audio.wav")
        self.assertEqual(result, "This is a test transcription.")

    @patch("whisper.load_model")
    def test_transcribe_audio_exception(self, mock_load_model):
        # Set up load_model to raise an exception
        mock_load_model.side_effect = Exception("Model load error")

        # Call the function and verify it handles the exception
        result = transcribe_audio("test_audio.wav")
        
        # Since we print the exception instead of returning, result should be None
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
