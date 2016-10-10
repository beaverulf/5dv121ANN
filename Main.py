import sys

from Perceptron import Perceptron
from ImageReader import ImageReader

def main(image_file=None, facit_file=None):

    image_reader = ImageReader()

    if image_file is not None:
        image_reader.parse_image_file(image_file)
    if facit_file and image_file is not None:
        image_reader.parse_facit_file(facit_file)
    else:
        print "Plz provide an image file"

    perceptrons = []
    perceptrons.append(Perceptron())

    for img in image_reader.images:
        perceptrons[0].train_perceptron(img)


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])