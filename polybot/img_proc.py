from pathlib import Path
from matplotlib.image import imread, imsave
import random


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path

    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

    def rotate(self):
        # TODO remove the `raise` below, and write your implementation
        # Rotate the image 90 degrees clockwise
        self.data = [[self.data[y][x] for y in reversed(range(len(self.data)))] for x in range(len(self.data[0]))]

    def salt_n_pepper(self):
        # TODO remove the `raise` below, and write your implementation
        # Apply salt and pepper noise
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                rnd = random.random()
                if rnd < 0.2:
                    self.data[y][x] = 255
                elif rnd > 0.8:
                    self.data[y][x] = 0

    def concat(self, other_img, direction='horizontal'):
        # TODO remove the `raise` below, and write your implementation
        # Concatenate another image horizontally or vertically
        if direction == "horizontal":
            if len(self.data) != len(other_img.data):
                raise RuntimeError("Images have different heights, cannot concatenate horizontally.")
            self.data = [self_row + other_row for self_row, other_row in zip(self.data, other_img.data)]
        elif direction == "vertical":
            if len(self.data[0]) != len(other_img.data[0]):
                raise RuntimeError("Images have different widths, cannot concatenate vertically.")
            self.data += other_img.data
        else:
            raise ValueError("Invalid direction; choose 'horizontal' or 'vertical'.")

    def segment(self):
        # TODO remove the `raise` below, and write your implementation
        # Segment the image based on intensity threshold
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                self.data[y][x] = 255 if self.data[y][x] > threshold else 0
