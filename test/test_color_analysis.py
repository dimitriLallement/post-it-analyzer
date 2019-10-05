import unittest
import post_it_color
from color_analysis import *

class TestColorAnalysisMethods(unittest.TestCase):
    """Tests of the color analysis methods"""

    def test_most_frequent_color(self):
        """Check if the most frequent color is the good one"""

        postItTest = nearest_color("test/img/yellow.png")
        self.assertIsNotNone(postItTest)
        self.assertIsInstance(postItTest, post_it_color.PostItColor)
        self.assertEqual(postItTest.rgb, [255, 255, 0])
        self.assertEqual(postItTest.color, "yellow")
        self.assertEqual(postItTest.type, "done")


if __name__ == '__main__':
    unittest.main()