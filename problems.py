import numpy as np
import math


class Problem1:
    def __init__(self):
        self.interval = [-100, 100]

    def objectiveFunction(self, x):
        return (pow(x, 2) / 100) + (10 * math.sin(x - (math.pi / 2)))

    def getNextNeighbor(self, currentState):
        nextNeighbor = currentState + np.random.randn()
        if nextNeighbor < self.interval[0] or nextNeighbor > self.interval[1]:
            return self.restart()
        else:
            return nextNeighbor

    def restart(self):
        return np.random.uniform(self.interval[0], self.interval[1])

    def crossover(self, parents):
        alfa = np.random.normal(0.0, 0.1)

        state2 = (parents[0].value * alfa) + parents[1].value * (1 - alfa)
        state2 = (parents[1].value * alfa) + parents[0].value * (1 - alfa)

        return [state2, state2]
