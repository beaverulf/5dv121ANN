import random
import math


class Perceptron:

    #goal of the perceptron
    face_facit = 2

    #learning rate
    alpha = 0.5

    #the weights of each link
    weights = []

    def init_weights(self):
        for i in range(0,20) :
            self.weights.append([])
            for j in range(0,20):
                self.weights[i].append(random.random())

    def __init__(self):
        self.init_weights()

    def train_perceptron(self,training_image):
        for k in range(0,20):
            sum = 0.0
            for j in range(0,20) :
                for i in range(0,20):
                   sum += float(training_image.pixels[j][i]) * self.weights[j][i]
            sum = sum/400

            error = float(training_image.image_facit)/4 - self.sigmoid(sum)

            for j in range(0,20) :
                for i in range(0,20):
                    self.weights[i][j] += self.alpha*error*float(training_image.pixels[j][i])

        print error

    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))

