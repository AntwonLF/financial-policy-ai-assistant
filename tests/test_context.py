
import unittest
from src.context import build_context


class TestBuildContext(unittest.TestCase):

    def test_context_formatting(self):
        results = [
            {
                "source": "policy.txt",
                "section": "Account Termination",
                "text": "Disable accounts within 24 hours."
            },
            {
                "source": "policy.txt",
                "section": "Access Reviews",
                "text": "Review access every 90 days."
            }
        ]

        context = build_context(results)

        self.assertIn("Source: policy.txt", context)
        self.assertIn("Section: Account Termination", context)
        self.assertIn("Disable accounts within 24 hours.", context)
        self.assertIn("\n\n---\n\n", context)
        self.assertEqual(context.count("Source:"), 2)

    def test_empty_results(self):
        context = build_context([])

        self.assertEqual(
            context,
            "No relevant policy sections were retrieved."
        )


if __name__ == "__main__":
    unittest.main()
