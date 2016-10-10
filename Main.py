import sys

from ImageReader import ImageReader

def main(image_file=None):

    image_reader = ImageReader()

    if image_file is not None:
        image_reader.read_image(image_file)
        #image = image_reader.images[]
       # image.print_pixel_matrix()
    else:
        print "Plz provide an image file"

if __name__ == '__main__':
    main(sys.argv[1])