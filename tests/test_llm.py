
import unittest
from unittest.mock import patch

from src.llm import generate_answer


class TestLLM(unittest.TestCase):

    @patch("src.llm.chat")
    def test_generate_answer(self, mock_chat):

        # Simulate a response from Llama 3.2
        mock_chat.return_value.message.content = (
            "Accounts must be disabled within 24 hours."
        )

        # Call our LLM function
        answer = generate_answer("Test policy prompt")

        # Verify the returned answer
        self.assertEqual(
            answer,
            "Accounts must be disabled within 24 hours."
        )

        # Verify the correct model and prompt were used
        mock_chat.assert_called_once_with(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": "Test policy prompt"
                }
            ]
        )


if __name__ == "__main__":
    unittest.main()
