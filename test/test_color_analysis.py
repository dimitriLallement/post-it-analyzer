import unittest
import post_it_color
import yaml
from PIL import Image
from color_analysis import nearest_color
from color_analysis import most_frequent_color
from color_analysis import load_config

class TestColorAnalysisMethods(unittest.TestCase):
    """Tests of the color analysis methods"""

    def test_nearest_color(self):
        """Check if the nearest color is the good one"""

        postItTest = nearest_color("test/img/yellow.png")
        self.assertIsNotNone(postItTest)
        self.assertIsInstance(postItTest, post_it_color.PostItColor)
        self.assertEqual(postItTest.rgb, [255, 255, 0])
        self.assertEqual(postItTest.color, "yellow")
        self.assertEqual(postItTest.type, "done")

    def test_most_frequent_color(self):
        """Check if the most frequent color is the good one"""
        
        image = Image.open("test/img/blue.png")
        rgb = most_frequent_color(image)
        self.assertIsNotNone(rgb)
        self.assertIsInstance(rgb, tuple)
        self.assertEqual(rgb, (45, 207, 254))

    def test_load_config(self):
        """Check the configuration file loading"""
        self.assertIsNotNone(load_config("test/color_config.yml"))

if __name__ == '__main__':
    unittest.main()