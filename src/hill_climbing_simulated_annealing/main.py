from math import sin, pi
from benchmarkable_algorithms.test import Test
from benchmarkable_algorithms.hill_climbing import HillClimbing
from benchmarkable_algorithms.iteractive_hill_climbing import InteractiveHillClimbing
from benchmarkable_algorithms.stochastic_hill_climbing import StochasticHillClimbing
from benchmarkable_algorithms.simulated_annealing import SimulatedAnnealing
from benchmarkable_algorithms.benchmark import Benchmark

MAX_ITERATIONS = 1000

def g(x:float) -> float:
    return 2**(-2 * (((x-0.1)/0.9)**2)) * (sin(5*pi*x)**6)

if __name__ == "__main__":
    a = HillClimbing(g, 0.001, MAX_ITERATIONS)
    a2 = InteractiveHillClimbing(g, 0.001, 100, MAX_ITERATIONS)
    a3 = StochasticHillClimbing(g, 0.01, 0.001, MAX_ITERATIONS)
    a4 = SimulatedAnnealing(g, 0.01, 1000, MAX_ITERATIONS)
    b =  Benchmark(a)
    b2 = Benchmark(a2)
    b3 = Benchmark(a3)
    b4 = Benchmark(a4)
    b.run()
    b2.run()
    b3.run()
    b4.run()