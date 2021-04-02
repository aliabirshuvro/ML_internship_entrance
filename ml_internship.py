# -*- coding: utf-8 -*-
"""ML internship.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ewsd6EQwdjnSFnYbCXpmD_XCas3IXad1
"""

import numpy as np
class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = relu(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * relu_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def sigmoid(z):
	      return 1.0/(1.0+np.exp(-z))
       
    def relu(z):
        res = z
			  for i in range(len(res)):
				    res[i] = max(0,res[i])
			  return res

    def sigmoid_derivative(z):
        sig = sigmoid(z)
			  return sig * (1 - sig)
    
    def relu_derivative(z):
        res = z
			  for i in range(len(res)):
				    if res[i] > 0:
					      res[i] = 1
				    else:
					      res[i] = 0
			  return res