from random import random
from math import exp
import numpy as np
from .base_algorithm import BaseAlgorithm

class SimulatedAnnealing(BaseAlgorithm):
    def __init__(self, evaluator, deviation, temperature:float, max_iterations:int = 10) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.deviation = deviation
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.x = []
    
    def __decrease_temperature(self):
        self.temperature = 0.8 * self.temperature

    def __algorithm(self) -> float:
        x = random()
        x_evaluated = self.evaluator(x)

        i = 0

        while i < self.max_iterations and self.temperature > 0.9:
            x_line = x + np.random.normal(scale=self.deviation)

            while x_line < 0:
                x_line = x + np.random.normal(scale=self.deviation)

            x_line_evaluated = self.evaluator(x_line)

            if x_line_evaluated > x_evaluated:
                x = x_line

            elif random() < (1/(1+exp(x_evaluated - x_line_evaluated)/self.temperature)):
                x = x_line

            self.__decrease_temperature()
            i += 1

        return x
    
    def run(self):
        x = self.__algorithm()
        print("Value of X: {} | g(x) = {}".format(x, self.evaluator(x)))
        self.x.append(x)

    def clean_memory(self):
        self.x.clear()