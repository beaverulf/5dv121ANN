class Image:

    def __init__(self):
        self.pixels = []
        self.image_facit = 0
        self.image_name = None


    def print_pixel_matrix(self):
        print self.image_name
        for line in self.pixels:
            print line

