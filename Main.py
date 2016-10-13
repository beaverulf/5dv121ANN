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
    happy_perceptron = Perceptron()
    sad_perceptron = Perceptron()
    mischievous_perceptron = Perceptron()
    mad_perceptron = Perceptron()

    perceptrons.append(happy_perceptron)
    perceptrons.append(sad_perceptron)
    perceptrons.append(mischievous_perceptron)
    perceptrons.append(mad_perceptron)



    for img in image_reader.images:
       print perceptrons[0].fire_perceptron(img)




if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])