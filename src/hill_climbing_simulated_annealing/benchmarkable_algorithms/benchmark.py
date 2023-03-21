import timeit
from .base_algorithm import BaseAlgorithm

class InvalidNumberOfRunsException(Exception):
    def __str__(self) -> str:
        return super().__str__("The number of runs must be greater than zero.")

class Benchmark:
    def __init__(self, algorithm:BaseAlgorithm, n_runs:int = 1) -> None:
        self.algorithm_name = algorithm.__class__.__name__
        self.algorithm_run = algorithm.run

        if n_runs > 0:
            self.n_runs = n_runs
        else:
            raise InvalidNumberOfRunsException

        self.time_elapsed = None
        pass

    def run(self, n_runs:int = 1) -> float:
        print("\n================= Benchmark Data ============================")
        print("Algorithm: {}\nN° of runs: {}".format(self.algorithm_name, n_runs))
        print("================== Runing algorithm =========================")
        duration = timeit.Timer(self.algorithm_run).timeit(n_runs)
        print("================== Benchmark results ========================")
        duration /= n_runs 
        duration *= 1000
        print("Time elapsed per run (ms): {}".format(duration))
        self.time_elapsed = duration
        print("================== End of the benchmark =====================\n")