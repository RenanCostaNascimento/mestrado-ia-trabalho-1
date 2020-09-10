import random
import numpy as np
from math import sin, pi, pow, cos, sqrt

standardDeviation = 2.0

class Problem1:
    def __init__(self):
        self.interval = [-100, 100]
        self.mutationChance = 0.3
        self.initialStates = [
            -88.42356534,
            -74.17652733,
            -96.04533575,
            -46.20975576,
            -51.08525224,
            84.25824009,
            89.62662973,
            62.71057724,
            41.82046817,
            74.48850765
        ]

    def objectiveFunction(self, x):
        return (pow(x, 2) / 100) + (10 * sin(x - (pi / 2)))

    def getNextNeighbor(self, currentState):
        nextNeighbor = currentState + np.random.normal(0.0, standardDeviation)
        if nextNeighbor < self.interval[0] or nextNeighbor > self.interval[1]:
            return self.restart()
        else:
            return nextNeighbor

    def restart(self):
        return np.random.uniform(self.interval[0], self.interval[1])

    def initialize(self, stateIndex):
        return self.initialStates[stateIndex]

    def crossover(self, parents):
        p1 = parents[0].state
        p2 = parents[1].state

        alfa1 = np.random.uniform(0.0, 1)
        state1 = (p1 * alfa1) + p2 * (1 - alfa1)

        alfa2 = np.random.uniform(0.0, 1)
        state2 = (p2 * alfa2) + p1 * (1 - alfa2)

        return [state1, state2]

    def mutation(self, child):
        if random.random() <= self.mutationChance:
            return self.getNextNeighbor(child)

        return child


class Problem2:
    def __init__(self):
        self.interval = [-5.12, 5.12]
        self.mutationChance = 0.3
        self.initialStates = [
            {"x": 29.51654484170328, "y": 78.65440951124137},
            {"x": 93.40606119162919, "y": 95.15017642984012},
            {"x": 85.73574673864115, "y": 46.1873470887395},
            {"x": 51.07598900888397, "y": 36.27029950966559},
            {"x": 87.24782796076327, "y": 57.140204016780096},
            {"x": -62.12861845683161, "y": -88.06454382247352},
            {"x": -96.79646051293301, "y": -96.59722486438855},
            {"x": -64.93822754620575, "y": -52.19933087484202},
            {"x": -10.749449541608, "y": -16.58523200298534},
            {"x": -70.53054054615664, "y": -98.1420602185348}
        ]

    def objectiveFunction(self, value):
        x = value.get("x")
        y = value.get("y")

        return 20 + (pow(x, 2) - 10 * cos(2 * pi * x)) + (pow(y, 2) - 10 * cos(2 * pi * y))

    def getNextNeighbor(self, currentState):
        nextNeighborX = currentState.get("x") + np.random.normal(0.0, standardDeviation)
        if nextNeighborX < self.interval[0] or nextNeighborX > self.interval[1]:
            nextNeighborX = self.getRandomValidValue()

        nextNeighborY = currentState.get("y") + np.random.normal(0.0, standardDeviation)
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

    def initialize(self, stateIndex):
        return self.initialStates[stateIndex]

    def getRandomValidValue(self):
        return np.random.uniform(self.interval[0], self.interval[1])

    def crossover(self, parents):
        x1 = parents[0].state.get("x")
        y1 = parents[0].state.get("y")
        x2 = parents[1].state.get("x")
        y2 = parents[1].state.get("y")

        alfa1 = np.random.uniform(0.0, 1)
        state1 = {
            "x": (x1 * alfa1) + x2 * (1 - alfa1),
            "y": (y1 * alfa1) + y2 * (1 - alfa1),
        }

        alfa2 = np.random.uniform(0.0, 1)
        state2 = {
            "x": (x2 * alfa2) + x1 * (1 - alfa2),
            "y": (y2 * alfa2) + y1 * (1 - alfa2),
        }

        return [state1, state2]

    def mutation(self, child):
        if random.random() <= self.mutationChance:
            return self.getNextNeighbor(child)

        return child


class Problem3:
    def __init__(self, cities):
        self.cities = cities
        self.mutationChance = 0.15

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
        citiesCopy = self.cities.copy()
        random.shuffle(citiesCopy)
        return citiesCopy

    def initialize(self, stateIndex):
        seedForRerandomization = np.random.randint(0, 1e6)
        np.random.seed(1)
        initialSolution = np.random.permutation(self.cities.copy())
        np.random.seed(seedForRerandomization)
        return list(initialSolution)

    def crossover(self, parents):
        cutPoint = random.randint(1, len(parents[0].state) - 2)
        child1 = self.generateChild(cutPoint, parents[0], parents[1])
        child2 = self.generateChild(cutPoint, parents[1], parents[0])

        return [child1, child2]

    def generateChild(self, cutPoint, parent1, parent2):
        parentSize = len(parent1.state)
        genes1 = parent1.state[cutPoint:parentSize]
        genes2 = []
        index = 0
        sizeGenes2 = parentSize - len(genes1)
        while len(genes2) != sizeGenes2:
            if parent2.state[index] not in genes1:
                genes2.append(parent2.state[index])
            index += 1

        return genes2 + genes1

    def mutation(self, child):
        if random.random() <= self.mutationChance:
            return self.getNextNeighbor(child)

        return child

def testProblem3():
    cities = [
        {'city': 1, 'x': 20833.3333, 'y': 17100.0},
        {'city': 2, 'x': 20900.0, 'y': 17066.6667},
        {'city': 3, 'x': 21300.0, 'y': 13016.6667},
        {'city': 4, 'x': 21600.0, 'y': 14150.0},
        {'city': 5, 'x': 21600.0, 'y': 14966.6667},
        {'city': 6, 'x': 21600.0, 'y': 16500.0},
        {'city': 7, 'x': 22183.3333, 'y': 13133.3333},
        {'city': 8, 'x': 22583.3333, 'y': 14300.0},
        {'city': 9, 'x': 22683.3333, 'y': 12716.6667},
        {'city': 10, 'x': 23616.6667, 'y': 15866.6667},
        {'city': 11, 'x': 23700.0, 'y': 15933.3333},
        {'city': 12, 'x': 23883.3333, 'y': 14533.3333},
        {'city': 13, 'x': 24166.6667, 'y': 13250.0},
        {'city': 14, 'x': 25149.1667, 'y': 12365.8333},
        {'city': 15, 'x': 26133.3333, 'y': 14500.0},
        {'city': 16, 'x': 26150.0, 'y': 10550.0},
        {'city': 17, 'x': 26283.3333, 'y': 12766.6667},
        {'city': 18, 'x': 26433.3333, 'y': 13433.3333},
        {'city': 19, 'x': 26550.0, 'y': 13850.0},
        {'city': 20, 'x': 26733.3333, 'y': 11683.3333},
        {'city': 21, 'x': 27026.1111, 'y': 13051.9444},
        {'city': 22, 'x': 27096.1111, 'y': 13415.8333},
        {'city': 23, 'x': 27153.6111, 'y': 13203.3333},
        {'city': 24, 'x': 27166.6667, 'y': 9833.3333},
        {'city': 25, 'x': 27233.3333, 'y': 10450.0},
        {'city': 26, 'x': 27233.3333, 'y': 11783.3333},
        {'city': 27, 'x': 27266.6667, 'y': 10383.3333},
        {'city': 28, 'x': 27433.3333, 'y': 12400.0},
        {'city': 29, 'x': 27462.5, 'y': 12992.2222},
    ]

    p1 = Problem3(cities)
    citiesCopy = cities.copy()
    random.shuffle(citiesCopy)
    p2 = Problem3(citiesCopy)

    s1 = 1
    s2 = 2

    while s2 > s1:
        s1 = p1.objectiveFunction(cities)
        s2 = p2.objectiveFunction(citiesCopy)
        random.shuffle(citiesCopy)
        print("\n", s1)
        print(s2)


# testProblem3()