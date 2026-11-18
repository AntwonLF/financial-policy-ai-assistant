
import tempfile
import unittest
from unittest.mock import patch

import chromadb
import numpy as np

from src.database import store_policy_chunks, search_stored_policies


class TestVectorDatabase(unittest.TestCase):

    def setUp(self):
        # Create a temporary database for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        client = chromadb.PersistentClient(path=self.temp_dir.name)

        self.collection = client.get_or_create_collection(
            name="test_policy_chunks",
            configuration={"hnsw": {"space": "cosine"}}
        )

        # Sample policy records
        self.records = [
            {
                "chunk_id": 1,
                "source": "test_policy.txt",
                "section": "Account Termination",
                "text": "Disable accounts within 24 hours."
            },
            {
                "chunk_id": 2,
                "source": "test_policy.txt",
                "section": "MFA",
                "text": "Employees must use MFA."
            }
        ]

        # Simple, controlled embeddings
        self.embeddings = np.array([
            [1.0, 0.0],
            [0.0, 1.0]
        ])

    def test_persistence_and_no_duplicates(self):
        store_policy_chunks(
            self.collection, self.records, self.embeddings
        )

        # Index the same records again
        store_policy_chunks(
            self.collection, self.records, self.embeddings
        )

        # Reopen the stored collection
        client = chromadb.PersistentClient(path=self.temp_dir.name)
        collection = client.get_collection("test_policy_chunks")

        self.assertEqual(collection.count(), 2)

    def test_retrieves_correct_section(self):
        store_policy_chunks(
            self.collection, self.records, self.embeddings
        )

        # Simulate a question embedding without loading the AI model
        with patch(
            "src.database.get_policy_collection",
            return_value=self.collection
        ), patch(
            "src.embeddings.generate_embeddings",
            return_value=np.array([[1.0, 0.0]])
        ):
            results = search_stored_policies(
                "When must accounts be disabled?",
                top_k=1
            )

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0]["section"],
            "Account Termination"
        )
        self.assertAlmostEqual(results[0]["similarity"], 1.0)


if __name__ == "__main__":
    unittest.main()
