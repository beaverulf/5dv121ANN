import random
import math

class Perceptron:

    def __init__(self, facit_value):
        self.consecutive_error_bound = 0.1
        self.cons_counter = 0
        self.cons_limit = 3

        # learning rate
        self.alpha = 0.06

        # the weights of each link
        self.weights = []

        self.face_facit = facit_value
        self.init_weights()

    def init_weights(self):
        for i in range(0,20) :
            self.weights.append([])
            for j in range(0,20):
                self.weights[i].append(0)

    def fire_perceptron(self, image):
        sum = 0.0
        for j in range(0, 20):
            for i in range(0, 20):
                sum += (float(image.pixels[j][i]) / 31) * self.weights[j][i]
        sum = sum / (20*20)
        return self.activation_func(sum)


    def compute_error(self,image,activation):
        #print self.face_facit, image.image_facit
        if self.face_facit == image.image_facit:
            error = 1.0 - activation
        else:
            error = 0.0 - activation
        return error

    def adjust_weights(self,error,image):
        for j in range(0,20) :
            for i in range(0,20):
                self.weights[i][j] += self.alpha*error*(float(image.pixels[j][i])/31)

    # Training algorithm for perceptron
    def train_perceptron(self, image):
        # Fire perceptron gives the activation from the sigmoid function.
        # This computes the error.
        activation = self.fire_perceptron(image)
        error = self.compute_error(image, activation)
        # adjusts the weights in the perceptron
        self.adjust_weights(error, image)

        if abs(error) <= self.consecutive_error_bound:
            self.cons_counter += 1
        else:
            self.cons_counter = 0
        return error

    def activation_func(self, x):
        #return 1 / (1 + math.exp(-x))
        return math.tanh(x)

