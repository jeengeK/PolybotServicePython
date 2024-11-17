import unittest
import random
from polybot.img_proc import Img
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'


class TestImgConcat(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.img = Img(img_path)
        cls.original_img = Img(img_path)

        cls.img.segment()

    def test_rotation_dimension(self):
        actual_dimension = (len(self.img.data), len(self.img.data[0]))
        expected_dimension = (len(self.original_img.data), len(self.original_img.data[0]))
        self.assertEqual(expected_dimension, actual_dimension)

    def test_black_white(self):
        bw_sum = all(pixel in [0, 255] for row in self.img.data for pixel in row)
        self.assertTrue(bw_sum)

    def test_segmentation_in_random_pixels(self):
        def segment(self):
            # The segment method will segment the image based on intensity.
            # Pixels with an intensity above a certain threshold (100) will be set to white, while others will be set to black.
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    # Set pixel to white if above threshold, otherwise black
                    self.data[i][j] = 255 if self.data[i][j] > 100 else 0





