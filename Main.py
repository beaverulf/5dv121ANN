import sys

from ImageReader import ImageReader

def main(image_file=None, facit_file=None):

    image_reader = ImageReader()

    if image_file is not None:
        image_reader.parse_image_file(image_file)

    if facit_file and image_file is not None:
        image_reader.parse_facit_file(facit_file)
    else:
        print "Plz provide an image file"

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])