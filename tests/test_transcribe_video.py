import unittest
from unittest.mock import patch, MagicMock
from services.transcribe.transcribe_video import transcribe_video

class TestTranscribeVideo(unittest.TestCase):

    @patch("services.transcribe.transcribe_audio.transcribe_audio")
    @patch("moviepy.editor.VideoFileClip")
    def test_transcribe_video_success(self, mock_video_clip, mock_transcribe_audio):
        # Setup mock objects
        mock_video = MagicMock()
        mock_audio = MagicMock()

        mock_video.audio = mock_audio
        mock_video_clip.return_value = mock_video
        mock_transcribe_audio.return_value = "This is a test transcription."

        # Mock write_audiofile to avoid actual file creation
        mock_audio.write_audiofile = MagicMock()

        # Call the function
        result = transcribe_video("test_video.mp4")

        # Assertions
        mock_video_clip.assert_called_once_with("test_video.mp4")
        mock_audio.write_audiofile.assert_called_once_with("test_video.mp4.wav")
        #mock_transcribe_audio.assert_called_once_with("test_video.mp4.wav")
        self.assertEqual(result, "This is a test transcription.")

        # Ensure resources are closed
        #mock_video.close.assert_called_once()

    @patch("moviepy.editor.VideoFileClip")
    def test_transcribe_video_no_audio(self, mock_video_clip):
        # Setup mock video with no audio
        mock_video = MagicMock()
        mock_video.audio = None
        mock_video_clip.return_value = mock_video

        # Call the function and verify it raises an error due to no audio
        with self.assertRaises(AttributeError):
            transcribe_video("test_video.mp4")

        # Ensure resources are closed
        #mock_video.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
