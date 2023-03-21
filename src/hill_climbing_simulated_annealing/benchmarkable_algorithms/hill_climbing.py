from random import random
import numpy as np
from .base_algorithm import BaseAlgorithm

class HillClimbing(BaseAlgorithm):
    def __init__(self, evaluator, deviation, max_iterations:int = 10,) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.deviation = deviation
        self.max_iterations = max_iterations
        self.x = None
    
    def __algorithm(self) -> float:
        x = random()
        x_evaluated = self.evaluator(x)

        for i in range(self.max_iterations):
            x_line = x + np.random.normal(scale=self.deviation)

            while x_line < 0:
                x_line = x + np.random.normal(scale=self.deviation)

            x_line_evaluated = self.evaluator(x_line)

            if x_line_evaluated > x_evaluated:
                x = x_line

        return x
    
    def run(self):
        x = self.__algorithm()
        print("Value of X: {} | g(x) = {}".format(x, self.evaluator(x)))
        self.x = x
