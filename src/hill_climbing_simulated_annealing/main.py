from math import sin, pi
import numpy as np
import matplotlib.pyplot as plt
from benchmarkable_algorithms.hill_climbing import HillClimbing
from benchmarkable_algorithms.iteractive_hill_climbing import InteractiveHillClimbing
from benchmarkable_algorithms.stochastic_hill_climbing import StochasticHillClimbing
from benchmarkable_algorithms.simulated_annealing import SimulatedAnnealing
from benchmarkable_algorithms.benchmark import Benchmark

MAX_ALGORITHM_ITERATIONS = 1000
GAUSIAN_NOISE_DEVIATION = 0.01
INTERACTIVE_ALGORITHM_INTERATIONS = 100
TEMPERATURE = 1000

BENCHMARK_N_EXECUTIONS = 1000

def g(x:float) -> float:
    return 2**(-2 * (((x-0.1)/0.9)**2)) * (sin(5*pi*x)**6)

if __name__ == "__main__":

    algorithms = []
    benchmarks = []

    hc = HillClimbing(g, GAUSIAN_NOISE_DEVIATION, MAX_ALGORITHM_ITERATIONS)
    hb_benchmark = Benchmark(hc)
    algorithms.append(hc)
    benchmarks.append(hb_benchmark) 

    ihc = InteractiveHillClimbing(g, GAUSIAN_NOISE_DEVIATION, INTERACTIVE_ALGORITHM_INTERATIONS, MAX_ALGORITHM_ITERATIONS)
    ihc_benchmark = Benchmark(ihc)
    algorithms.append(ihc)
    benchmarks.append(ihc_benchmark)

    shc = StochasticHillClimbing(g, GAUSIAN_NOISE_DEVIATION, max_iterations=MAX_ALGORITHM_ITERATIONS)
    shc_benchmark = Benchmark(shc)
    algorithms.append(shc)
    benchmarks.append(shc_benchmark)

    sa = SimulatedAnnealing(g, GAUSIAN_NOISE_DEVIATION, TEMPERATURE, MAX_ALGORITHM_ITERATIONS)
    sa_benchmark = Benchmark(sa)
    algorithms.append(sa)
    benchmarks.append(sa_benchmark)

    mean_times_ms = []
    algorithm_names = []

    for benchmark in benchmarks:
        benchmark.run_multiple(BENCHMARK_N_EXECUTIONS)
        mean_times_ms.append(benchmark.elapsed_time_ms)
        algorithm_names.append(benchmark.algorithm_name)
    

    plt.figure(figsize=(10,6))
    plt.bar(algorithm_names, mean_times_ms, align="center", width=0.4)
    plt.title("Mean execution time of all algorithms ({} executions)".format(BENCHMARK_N_EXECUTIONS))
    plt.ylabel("Time (ms)")
    plt.xlabel("Algorithm")
    plt.savefig("foo.png")

    mean_times_ms.remove(np.max(mean_times_ms))
    algorithm_names.remove(ihc.__class__.__name__)

    plt.figure(figsize=(10,6))
    plt.bar(algorithm_names, mean_times_ms, align="center", width=0.4)
    plt.title("Mean execution time without Interactive Hill Climbing for better scale ({} executions)".format(BENCHMARK_N_EXECUTIONS))
    plt.ylabel("Time (ms)")
    plt.xlabel("Algorithm")
    plt.savefig("bar.png")

    best_x = algorithms[0].x[0]
    best_algorithm = ""

    for algorithm in algorithms:
        for x in algorithm.x:
            if g(x) > g(best_x):
                best_x = x
                best_algorithm = algorithm.__class__.__name__

    print("Best {} | x: {} | g(x) = {}".format(best_algorithm, best_x, g(best_x)))

    for algorithm in algorithms:
        best_x = algorithm.x[0]
        for x in algorithm.x:
            if g(x) > g(best_x):
                best_x = x
         
        print("Best for {} | x: {} | g(x) = {}".format(algorithm.__class__.__name__, best_x, g(best_x)))
    