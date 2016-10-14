import sys
import random

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

    images = image_reader.images

    perceptrons = []
    happy_perceptron = Perceptron(1)
    sad_perceptron = Perceptron(2)
    mischievous_perceptron = Perceptron(3)
    mad_perceptron = Perceptron(4)

    perceptrons.append(happy_perceptron)
    perceptrons.append(sad_perceptron)
    perceptrons.append(mischievous_perceptron)
    perceptrons.append(mad_perceptron)

    #Training the perceptron
    random.shuffle(images)
    for i in range(0, 14):
        for perceptron in perceptrons:
            for k in range(0,200):
                perceptron.train_perceptron(images[k])

    ####################################

    #########TESTING PERCEPTRONS########
    correct = 0.0
    for i in range(0,100):
        curr_max = 0.0
        answer_face = 0
        for perceptron in perceptrons:
            activation = perceptron.fire_perceptron(images[i])
            if activation > curr_max:
                curr_max = activation
                answer_face = perceptron.face_facit

        if images[i].image_facit == answer_face:
            correct += 1
        #print images[i].image_name, activation
        #print "########################################"
            #if (1 - activation) <= 0.2:
    print correct/100


    ####################################



if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])