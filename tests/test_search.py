
import unittest
import numpy as np
from unittest.mock import patch

from src.search import search_policies


class TestSemanticSearch(unittest.TestCase):

    def setUp(self):
        # Sample records for testing
        self.records = [
            {
                "section": "MFA",
                "source": "test_policy.txt",
                "text": "Employees must use MFA."
            },
            {
                "section": "Account Termination",
                "source": "test_policy.txt",
                "text": "Disable accounts after termination."
            }
        ]

        # Simple 2D vectors to test ranking logic
        self.embeddings = np.array([
            [0.0, 1.0],
            [1.0, 0.0]
        ])

    @patch("src.search.generate_embeddings")
    def test_returns_most_relevant_section(self, mock_generate):
        # Simulate the question's embedding
        mock_generate.return_value = np.array([[1.0, 0.0]])

        results = search_policies(
            "When should accounts be disabled?",
            self.records,
            self.embeddings,
            top_k=1
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["section"], "Account Termination")
        self.assertAlmostEqual(results[0]["similarity"], 1.0)

    def test_empty_question(self):
        results = search_policies(
            "",
            self.records,
            self.embeddings
        )

        self.assertEqual(results, [])

    def test_mismatched_records(self):
        with self.assertRaises(ValueError):
            search_policies(
                "Employee access",
                self.records,
                self.embeddings[:1]
            )


if __name__ == "__main__":
    unittest.main()
