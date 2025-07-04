import unittest
import json
import os
from unittest.mock import patch

from main import extract_metadata, get_unified_tags, process_posts
from langchain_core.exceptions import OutputParserException


class TestErrorHandling(unittest.TestCase):

    def test_invalid_json_response(self):
        # Simulate invalid JSON from LLM
        with patch("main.llm") as mock_llm:
            mock_llm.invoke.return_value.content = "This is not a JSON!"
            with self.assertRaises(OutputParserException):
                extract_metadata("Sample post")

    def test_llm_failure_simulation(self):
        with patch("main.llm") as mock_llm:
            mock_llm.invoke.side_effect = Exception("Simulated failure")
            with self.assertRaises(Exception):
                get_unified_tags([{"tags": ["Motivation"]}])

    def test_corrupted_file_handling(self):
        # Create a dummy corrupted file
        corrupted_path = "corrupted.json"
        with open(corrupted_path, "wb") as f:
            f.write(b'{"text": "This post contains invalid chars: \x80\x81"}')

        try:
            process_posts(corrupted_path, "output.json")
            self.assertTrue(os.path.exists("output.json"))
        finally:
            os.remove(corrupted_path)
            if os.path.exists("output.json"):
                os.remove("output.json")

    def test_extract_metadata_fallback(self):
        # Simulate partial metadata response (missing keys)
        with patch("main.llm") as mock_llm:
            mock_llm.invoke.return_value.content = '{"line_count": 3}'
            with self.assertRaises(OutputParserException):
                extract_metadata("Incomplete metadata post")


if __name__ == '__main__':
    unittest.main()
