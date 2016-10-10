from Image import Image

class ImageReader:

    images = []


    def read_image(self,image_file):
        x = 0
        y = 0

        file = open(image_file)
        mat = []
        image_index = -1
        for line in file.readlines():
            if line.startswith('#') or len(line) <=1:
                continue
            if line.startswith("Image"):
                image_index +=1
                img = Image()
                img.image_name = line
                self.images.append(img)
            else:
                print image_index
                self.images[image_index].pixels.append(line.split())

















