import unittest
from services.transcribe.transcribe_audio import transcribe_audio
import os

class TestTranscribeAudioIntegration(unittest.TestCase):

    def test_transcribe_audio_with_real_file(self):
        # Path to an actual test audio file (must exist in the test directory)
        file_path = "path/to/test_audio.wav"
        
        # Call the function with a real audio file
        result = transcribe_audio(file_path)
        
        # Ensure the transcription result is a non-empty string
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0, "Transcription should not be empty")

if __name__ == "__main__":
    unittest.main()
