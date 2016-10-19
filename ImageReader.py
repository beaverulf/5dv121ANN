"""
Class with functionality to read and parse data from given textfiles.
"""
from Image import Image

class ImageReader:

    images = []
    test = []

    """
    Method to parse an image file for training.
    """
    def parse_image_file(self, image_file):
        image_index = -1
        for line in open(image_file).readlines():
            if line.startswith('#') or len(line) <=1:
                continue
            if line.startswith("Image"):
                image_index +=1
                img = Image()
                img.image_name = line
                self.images.append(img)
            else:
                self.images[image_index].pixels.append(line.split())

    """
    Method to parse a facit file
    """
    def parse_facit_file(self, facit_file):
        image_index = 0
        for line in open(facit_file).readlines():
            if line.startswith('#') or len(line) <= 1:
                continue
            if line.startswith("Image"):
                self.images[image_index].image_facit = int(line.split()[1])
                image_index += 1

    """
    Method to parse the test file
    """
    def parse_test_file(self, image_file):
        image_index = -1
        for line in open(image_file).readlines():
            if line.startswith('#') or len(line) <=1:
                continue
            if line.startswith("Image"):
                image_index +=1
                img = Image()
                img.image_name = line
                self.test.append(img)
            else:
                self.test[image_index].pixels.append(line.split())















