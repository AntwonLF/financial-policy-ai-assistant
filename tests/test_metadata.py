import unittest
from src.metadata import add_metadata       

class TestMetadata(unittest.TestCase):

    def test_metadata_creation(self):
        chunks = [
            "1. Employee Access\nManager approval required.",
            "2. MFA\nMulti-factor authentication required."
        ]

        records = add_metadata(chunks, "access_control_policy.txt")

        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["chunk_id"], 1)
        self.assertEqual(records[0]["source"], "access_control_policy.txt")
        self.assertEqual(records[0]["section"], "1. Employee Access")
        self.assertEqual(records[1]["section"], "2. MFA")


if __name__ == "__main__":
    unittest.main()

