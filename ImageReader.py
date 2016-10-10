from Image import Image

class ImageReader:

    images = []

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

















