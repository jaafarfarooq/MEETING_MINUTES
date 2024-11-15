import unittest
from services.chatgpt_response.get_chatgpt_response import get_chatgpt_response

class TestGetChatGptResponseIntegration(unittest.TestCase):

    def test_get_chatgpt_response_real_call(self):
        # Set up an actual prompt to test the integration with OpenAI's API
        result = get_chatgpt_response(" We discussed project timelines and deliverables in our meeting.")
        
        # Check that the result is a non-empty string (assuming successful transcription)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0, "The response should not be empty")

if __name__ == "__main__":
    unittest.main()
