import random
import numpy as np
from math import sin, pi, pow, cos, sqrt


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
        p1 = parents[0].state
        p2 = parents[1].state

        alfa1 = np.random.normal(0.0, 0.1)
        state1 = (p1 * alfa1) + p2 * (1 - alfa1)

        alfa2 = np.random.normal(0.0, 0.1)
        state2 = (p2 * alfa2) + p1 * (1 - alfa2)

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
        x1 = parents[0].state.get("x")
        y1 = parents[0].state.get("y")
        x2 = parents[1].state.get("x")
        y2 = parents[1].state.get("y")

        alfa1 = np.random.normal(0.0, 0.1)
        state1 = {
            "x": (x1 * alfa1) + x2 * (1 - alfa1),
            "y": (y1 * alfa1) + y2 * (1 - alfa1),
        }

        alfa2 = np.random.normal(0.0, 0.1)
        state2 = {
            "x": (x2 * alfa2) + x1 * (1 - alfa2),
            "y": (y2 * alfa2) + y1 * (1 - alfa2),
        }

        return [state1, state2]


class Problem3:
    def __init__(self, cities):
        self.cities = cities

    def objectiveFunction(self, cities):
        citiesCopy = cities.copy()
        citiesCopy.append(cities[0])
        totalCost = 0
        for index in range(len(citiesCopy) - 1):
            x1 = citiesCopy[index].get("x")
            y1 = citiesCopy[index].get("y")
            x2 = citiesCopy[index + 1].get("x")
            y2 = citiesCopy[index + 1].get("y")
            totalCost += sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        return totalCost

    def getNextNeighbor(self, cities):
        city1 = city2 = 0
        maxRandom = len(cities) - 1
        while(city1 == city2):
            city1 = random.randint(0, maxRandom)
            city2 = random.randint(0, maxRandom)

        citiesCopy = cities.copy()
        citiesCopy[city1] = cities[city2]
        citiesCopy[city2] = cities[city1]

        return citiesCopy

    def restart(self):
        return self.cities
