import time
from numpy import mean
from .base_algorithm import BaseAlgorithm

class InvalidNumberOfRunsException(Exception):
    def __str__(self) -> str:
        return super().__str__("The number of runs must be greater than zero.")

class Benchmark:
    def __init__(self, algorithm:BaseAlgorithm) -> None:
        self.algorithm_object = algorithm
        self.algorithm_name = algorithm.__class__.__name__
        self.algorithm_run = algorithm.run
        self.elapsed_time_ms = None
        pass

    def run(self) -> float:
        print("================== Runing {} algorithm =========================".format(self.algorithm_name))
        start = time.time()
        self.algorithm_run()
        end = time.time()
        print("================== Benchmark results ========================")
        duration = (end - start) 
        duration *= 1000
        print("Time elapsed per run (ms): {}".format(duration))
        self.elapsed_time_ms = duration
        print("================== End of the benchmark =====================\n")

    def run_multiple(self, n_runs:int = 10):
        if n_runs <= 0:
            raise InvalidNumberOfRunsException

        execution_times_ms = []

        print("================== Runing {} algorithm =========================".format(self.algorithm_name))

        for i in range(n_runs):
            start = time.time()
            self.algorithm_run()
            end = time.time()
            duration = (end - start) 
            duration *= 1000
            execution_times_ms.append(duration)
            print("Elapsed time on the {}° run (ms): {}".format(i+1, duration))

        print("================== Benchmark results ========================")
        print("Mean time ({} executions) (ms): {}".format(i+1, mean(execution_times_ms)))
        print("================== End of the benchmark =====================\n")
        self.elapsed_time_ms = mean(execution_times_ms)

