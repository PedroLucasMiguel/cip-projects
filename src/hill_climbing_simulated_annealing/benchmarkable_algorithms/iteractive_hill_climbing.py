from random import random
import numpy as np
from .base_algorithm import BaseAlgorithm

class InteractiveHillClimbing(BaseAlgorithm):
    def __init__(self, evaluator, deviation, n_algorithm_interactions:int = 1, max_iterations:int = 10,) -> None:
        super().__init__()
        self.evaluator = evaluator
        self.deviation = deviation
        self.max_iterations = max_iterations
        self.n_algorithm_interactions = n_algorithm_interactions
        self.x = []
    
    def __hill_climbing(self) -> float:
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

    def __algorithm(self) -> float:
        best = random()

        for i in range(self.n_algorithm_interactions):
            x = self.__hill_climbing()
            
            if self.evaluator(x) > self.evaluator(best):
                best = x
        
        return best
        
    
    def run(self):
        x = self.__algorithm()
        print("Value of X: {} | g(x) = {}".format(x, self.evaluator(x)))
        self.x.append(x)

    def clean_memory(self):
        self.x.clear()
