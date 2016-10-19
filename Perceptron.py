"""
Represents an output node in the network. Will have a facit value to strive for.
"""

import random
import math

class Perceptron:

    def __init__(self, facit_value):
        self.consecutive_error_bound = 0.1
        self.cons_counter = 0
        self.cons_limit = 3

        # learning rate
        self.alpha = 0.2

        # the weights of each link
        self.weights = []

        self.face_facit = facit_value
        self.init_weights()

    """
    Method to initiate the weights. The weights recieve a random value
    between 0 and 1
    """
    def init_weights(self):
        for i in range(0,20) :
            self.weights.append([])
            for j in range(0,20):
                self.weights[i].append(random.random())

    """
    Method to fire the perceptron. Returns the activation value.
    """
    def fire_perceptron(self, image):
        sum = 0.0
        for j in range(0, 20):
            for i in range(0, 20):
                sum += (float(image.pixels[j][i]) / 31) * self.weights[j][i]
        return self.activation_func(sum)

    """
    Method to compute the error of the activation value.
    """
    def compute_error(self,image,activation):
        if self.face_facit == image.image_facit:
            error = 1.0 - activation
        else:
            error = 0.0 - activation
        return error

    """
    Method to adjust the weights given an error value
    """
    def adjust_weights(self,error,image):
        for j in range(0,20) :
            for i in range(0,20):
                self.weights[j][i] += self.alpha*error*(float(image.pixels[j][i])/31)

    """
    The rraining algorithm for the perceptron
    """
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

    """
    The activation function of the perceptron. Sigmoid is chosen for the task.
    """
    def activation_func(self, x):
        return 1 / (1 + math.exp(-x))


