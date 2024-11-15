import unittest
import os
from services.transcribe.transcribe_video import transcribe_video

class TestTranscribeVideoIntegration(unittest.TestCase):

    def test_transcribe_video_with_real_file(self):
        # Path to an actual test video file (must exist in the test directory)
        file_path = "test_video.mp4"
        
        # Call the function with a real video file
        result = transcribe_video(file_path)
        
        # Ensure transcription result is a string (basic check)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0, "Transcription should not be empty")

        # Check if the temporary audio file was created and remove it
        audio_file_path = file_path + ".wav"
        self.assertTrue(os.path.exists(audio_file_path), "Audio file should have been created")
        os.remove(audio_file_path)

if __name__ == "__main__":
    unittest.main()
