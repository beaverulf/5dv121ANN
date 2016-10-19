import sys
import random

from Perceptron import Perceptron
from ImageReader import ImageReader

def main(image_file=None, facit_file=None,test_file=None):

    image_reader = ImageReader()

    if image_file and facit_file and test_file is not None:
        image_reader.parse_image_file(image_file)
        image_reader.parse_facit_file(facit_file)
        image_reader.parse_test_file(test_file)
    else:
        print "faces.py training-file.txt training-facit.txt test-file.txt"

    images = image_reader.images

    # Initiates the perceptrons
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
    train = True
    loops = 0
    while(train == True):
       random.shuffle(images)
       for perceptron in perceptrons:
            for k in range(0, len(images)):
                perceptron.train_perceptron(images[k])
       train = False
       for perceptron in perceptrons:
           if perceptron.cons_counter < 2 or loops < 16:
               train = True
       loops = loops + 1
    ####################################

    #########TESTING PERCEPTRONS########
    test = image_reader.test
    for i in range(0,len(test)):
        curr_max = 0.0
        answer_face = 0
        for perceptron in perceptrons:
            activation = perceptron.fire_perceptron(test[i])
            if activation > curr_max:
                curr_max = activation
                answer_face = perceptron.face_facit
        print 'Image' +  str(i + 1), answer_face
    print '#loops ', loops

    ####################################

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print "faces.py training-file.txt training-facit.txt test-file.txt"
    else:
        main(sys.argv[1],sys.argv[2], sys.argv[3])