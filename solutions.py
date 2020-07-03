import random
import numpy as np
from functools import reduce


class Solution:
    def __init__(self, problem, state=None):
        self.state = state if state else problem.restart()
        self.value = problem.objectiveFunction(self.state)
        self.problem = problem

    def __str__(self):
        return "State: %f, Value: %f" % (self.state, self.value)

    def setState(self, newState):
        self.state = newState
        self.value = self.problem.objectiveFunction(newState)


def hillClimbing(problem):
    iterations = 0
    solution = Solution(problem)
    currentState = solution.state
    allValues = []
    allBestValues = []

    while iterations < 1000:
        nextNeighbor = problem.getNextNeighbor(currentState)
        currentValue = problem.objectiveFunction(nextNeighbor)
        allValues.append(currentValue)
        if currentValue < solution.value:
            solution.value = currentValue
            solution.state = nextNeighbor
            allBestValues.append(currentValue)
        else:
            allBestValues.append(solution.value)
        iterations += 1
        currentState = nextNeighbor

    output = {
        "solution": solution,
        "allValues": allValues,
        "allBestValues": allBestValues
    }
    return output


def randomRestartHillClimbing(problem):
    iterations = 0
    solution = Solution(problem)
    currentState = solution.state
    allValues = []
    allBestValues = []

    while iterations < 1000:
        if iterations % 50 == 0:
            nextNeighbor = problem.restart()
        else:
            nextNeighbor = problem.getNextNeighbor(currentState)
        currentValue = problem.objectiveFunction(nextNeighbor)
        allValues.append(currentValue)
        if currentValue < solution.value:
            solution.value = currentValue
            solution.state = nextNeighbor
            allBestValues.append(currentValue)
        else:
            allBestValues.append(solution.value)
        iterations += 1
        currentState = nextNeighbor

    output = {
        "solution": solution,
        "allValues": allValues,
        "allBestValues": allBestValues
    }
    return output


def simulatedAnneling(problem):
    iterations = 0
    solution = Solution(problem)
    currentState = solution.state
    temperature = 1

    allValues = []
    allBestValues = []

    while iterations < 1000:
        nextNeighbor = problem.getNextNeighbor(currentState)
        currentValue = problem.objectiveFunction(nextNeighbor)
        allValues.append(currentValue)
        if currentValue < solution.value:
            solution.value = currentValue
            solution.state = nextNeighbor
            allBestValues.append(currentValue)
        else:
            allBestValues.append(solution.value)
            if round(random.random(), 5) < temperature:
                solution.value = currentValue
                solution.state = nextNeighbor

        iterations += 1
        currentState = nextNeighbor
        temperature = cooling(temperature, 900)

    output = {
        "solution": solution,
        "allValues": allValues,
        "allBestValues": allBestValues
    }
    return output


def cooling(currentTemperature, freezingTime):
    factor = 1 / freezingTime
    newTemperature = currentTemperature - factor
    if newTemperature < 0:
        return 0
    else:
        return round(newTemperature, 5)


def testCooling(freezingTime, iterations):
    temperature = 1
    for i in range(iterations):
        temperature = cooling(temperature, freezingTime)
        print(temperature)


def geneticAlgorithm(problem):
    populationSize = 20
    generations = 50
    population = []

    allValues = []

    for individual in range(populationSize):
        population.append(Solution(problem))

    for generation in range(generations):
        currentPopulation = []

        for individual in range(0, populationSize, 2):
            parents = chooseParents(population)
            childrenStates = problem.crossover(parents)
            currentPopulation.append(
                Solution(
                    problem, problem.mutation(childrenStates[0])
                )
            )
            currentPopulation.append(
                Solution(
                    problem, problem.mutation(childrenStates[1])
                )
            )

        population = currentPopulation
        allValues.append(list(map(
            lambda solution: solution.value,
            currentPopulation
        )))

    output = {
        "solution": reduce(
            (lambda x, y: x if x < y else y),
            map(lambda solution: solution.value, population)
        ),
        "allValues": allValues
        # TODO salvar todas as melhores soluções
    }

    return output


def chooseParents(population):
    parents = []
    randomMax = len(population) - 1

    for round in range(2):
        p1 = population[random.randint(0, randomMax)]
        p2 = population[random.randint(0, randomMax)]
        if p1.value < p2.value:
            parents.append(p1)
        else:
            parents.append(p2)

    return parents

# testCooling(90, 100)
# print()
