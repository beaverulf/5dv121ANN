class Image:


    pixels = []
    image_name = None

    def set_pixel(self,x,y,val):
        self.pixels[x][y] = val

    def print_pixel_matrix(self):
        print self.pixels
