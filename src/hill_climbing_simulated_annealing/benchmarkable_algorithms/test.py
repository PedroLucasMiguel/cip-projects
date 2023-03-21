from .base_algorithm import BaseAlgorithm

class Test(BaseAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def __algorithm(self):
        print(":P")

    def run(self):
        self.__algorithm()