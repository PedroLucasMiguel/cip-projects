from random import random
from math import exp
import numpy as np
from .base_algorithm import BaseAlgorithm

class StochasticHillClimbing(BaseAlgorithm):
    def __init__(self, evaluator, deviation, T:float = 0.01, max_iterations:int = 10,) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.deviation = deviation
        self.T = T
        self.max_iterations = max_iterations
        self.x = []
    
    def __algorithm(self) -> float:
        x = random()
        x_evaluated = self.evaluator(x)

        for i in range(self.max_iterations):
            x_line = x + np.random.normal(scale=self.deviation)

            while x_line < 0:
                x_line = x + np.random.normal(scale=self.deviation)

            x_line_evaluated = self.evaluator(x_line)

            if random() < (1/(1+exp(x_evaluated - x_line_evaluated)/self.T)):
                x = x_line

        return x
    
    def run(self):
        x = self.__algorithm()
        print("Value of X: {} | g(x) = {}".format(x, self.evaluator(x)))
        self.x.append(x)

    def clean_memory(self):
        self.x.clear()