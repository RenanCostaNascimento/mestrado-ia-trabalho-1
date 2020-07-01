import numpy as np
from math import sin, pi, pow, cos


class Problem1:
    def __init__(self):
        self.interval = [-100, 100]

    def objectiveFunction(self, x):
        return (pow(x, 2) / 100) + (10 * sin(x - (pi / 2)))

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

        state1 = (parents[0].value * alfa) + parents[1].value * (1 - alfa)
        state2 = (parents[1].value * alfa) + parents[0].value * (1 - alfa)

        return [state1, state2]


class Problem2:
    def __init__(self):
        self.interval = [-5.12, 5.12]

    def objectiveFunction(self, value):
        x = value.get("x")
        y = value.get("y")

        return 20 + (pow(x, 2) - 10 * cos(2 * pi * x)) + (pow(y, 2) - 10 * cos(2 * pi * y))

    def getNextNeighbor(self, currentState):
        nextNeighborX = currentState.get("x") + np.random.randn()
        if nextNeighborX < self.interval[0] or nextNeighborX > self.interval[1]:
            nextNeighborX = self.getRandomValidValue()

        nextNeighborY = currentState.get("y") + np.random.randn()
        if nextNeighborY < self.interval[0] or nextNeighborY > self.interval[1]:
            nextNeighborY = self.getRandomValidValue()

        return {
            "x": nextNeighborX,
            "y": nextNeighborY
        }

    def restart(self):
        return {
            "x": self.getRandomValidValue(),
            "y": self.getRandomValidValue()
        }

    def getRandomValidValue(self):
        return np.random.uniform(self.interval[0], self.interval[1])

    def crossover(self, parents):
        alfa = np.random.normal(0.0, 0.1)

        state2 = (parents[0].value * alfa) + parents[1].value * (1 - alfa)
        state2 = (parents[1].value * alfa) + parents[0].value * (1 - alfa)

        return [state2, state2]
