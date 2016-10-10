import sys

from ImageReader import ImageReader

def main(image_file=None):

    image_reader = ImageReader()

    if image_file is not None:
        image_reader.parse_image_file(image_file)

        for image in image_reader.images:
            image.print_pixel_matrix()
    else:
        print "Plz provide an image file"

if __name__ == '__main__':
    main(sys.argv[1])