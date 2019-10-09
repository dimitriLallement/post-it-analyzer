import unittest
import os
from text_analysis import extract_text


class TestTextAnalysisMethods(unittest.TestCase):
    """Tests of the text analysis method"""

    def test_extract_text(self):
        """Check if the extracted text is the good one"""
        text = extract_text("test/img/yellow.png", "eng")
        self.assertEqual(text, "Analytics")
        self.assertFalse(os.path.exists('tmp.png'))

if __name__ == '__main__':
    unittest.main()