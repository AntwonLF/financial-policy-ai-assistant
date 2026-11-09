
import unittest
from src.prompts import build_prompt


class TestBuildPrompt(unittest.TestCase):

    def test_prompt_contains_question_and_context(self):
        question = "When must accounts be disabled?"
        context = (
            "Source: access_control_policy.txt\n"
            "Section: Account Termination\n"
            "Policy Text: Disable accounts within 24 hours."
        )

        prompt = build_prompt(question, context)

        self.assertIn(question, prompt)
        self.assertIn(context, prompt)
        self.assertIn("ANSWER:", prompt)

    def test_prompt_contains_safety_rules(self):
        prompt = build_prompt("What is the policy?", "Sample context")

        self.assertIn("Do not invent policy requirements.", prompt)
        self.assertIn("Include the source filename and section.", prompt)


if __name__ == "__main__":
    unittest.main()
