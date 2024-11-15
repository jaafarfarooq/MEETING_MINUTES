import unittest
from unittest.mock import patch, MagicMock
from services.chatgpt_response.get_chatgpt_response import get_chatgpt_response

class TestGetChatGptResponse(unittest.TestCase):

    @patch("openai.ChatCompletion.create")
    def test_get_chatgpt_response_success(self, mock_chat_completion):
        # Mock a successful API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message={"content": "This is a sample meeting summary."})]
        mock_chat_completion.return_value = mock_response

        # Call the function with a test prompt
        result = get_chatgpt_response(" Here is a transcript of our meeting.")
        
        # Assertions
        mock_chat_completion.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Act as a professional summary editor, \
Write a meeting minutes from the transcript. \
Add name of the participants \
Write in a simple way and detail key conclusions from the discussion. \
We have just finished our meeting here is our transcript. Here is a transcript of our meeting."}
            ],
            max_tokens=150,
            temperature=0.7
        )
        self.assertEqual(result, "This is a sample meeting summary.")

    @patch("openai.ChatCompletion.create")
    def test_get_chatgpt_response_error(self, mock_chat_completion):
        # Set up the mock to raise an exception
        mock_chat_completion.side_effect = Exception("API error")

        # Call the function and expect it to handle the exception
        result = get_chatgpt_response(" Here is a transcript of our meeting.")
        
        # Verify that the function returns None on error
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
