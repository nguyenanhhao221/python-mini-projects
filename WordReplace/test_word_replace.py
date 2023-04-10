import unittest
from unittest.mock import patch

from word_replace import replace_word


class TestWordReplace(unittest.TestCase):
    def test_empty_input(self):
        with patch("builtins.input", side_effect=["", "replacement"]):
            with self.assertRaises(ValueError):
                replace_word()

        with patch("builtins.input", side_effect=["replacement", ""]):
            with self.assertRaises(ValueError):
                replace_word()

    def test_word_replace(self):
        expected_output = "hello guys, I am hao, and hello hello hello"
        with patch("builtins.input", side_effect=["hi", "hello"]):
            output = replace_word()
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
