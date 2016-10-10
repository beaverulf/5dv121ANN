class Image:
    pixels = None
    image_name = None
    image_facit = None

    def __init__(self):
        self.pixels = []


    def print_pixel_matrix(self):
        print self.image_name
        for line in self.pixels:
            print line
