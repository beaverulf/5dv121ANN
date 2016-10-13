import random
import math


class Perceptron:

    #goal of the perceptron
    face_facit = None

    #learning rate
    alpha = 0.05

    #the weights of each link
    weights = []

    def __init__(self):
        self.init_weights()

    def init_weights(self):
        for i in range(0,20) :
            self.weights.append([])
            for j in range(0,20):
                self.weights[i].append(random.random())

    def fire_perceptron(self, image):
        sum = 0.0
        for j in range(0,20) :
            for i in range(0,20):
               sum += float(image.pixels[j][i]) * self.weights[j][i]
        return self.sigmoid(sum)

    def compute_error(self,image,activation):
        error = float(image.image_facit) - activation
        return error

    def adjust_weights(self,error):
        for j in range(0,20) :
            for i in range(0,20):
                self.weights[i][j] += self.alpha*error*float(training_image.pixels[j][i])
        print error

    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))

