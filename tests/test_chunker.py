
import unittest
from src.chunker import chunk_policy


class TestChunkPolicy(unittest.TestCase):

    def test_splits_paragraphs(self):
        text = "Employee Access\n\nMFA Required\n\nAccount Termination"

        expected = [
            "Employee Access",
            "MFA Required",
            "Account Termination"
        ]

        self.assertEqual(chunk_policy(text), expected)

    def test_empty_document(self):
        self.assertEqual(chunk_policy(""), [])


if __name__ == "__main__":
    unittest.main()
