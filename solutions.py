import random
import numpy as np
from functools import reduce


class Solution:
    def __init__(self, problem, execution, state=None):
        if state:
            self.state = state
        else:
            self.state = problem.initialize(execution) if execution >= 0 else problem.restart()
        self.value = problem.objectiveFunction(self.state)
        self.problem = problem

    def setState(self, newState):
        self.state = newState
        self.value = self.problem.objectiveFunction(newState)


def hillClimbing(problem, execution):
    iterations = 0
    solution = Solution(problem, execution)
    currentState = solution.state
    allValues = []
    allBestValues = []

    while iterations < 1000:
        nextNeighbor = problem.getNextNeighbor(currentState)
        currentValue = problem.objectiveFunction(nextNeighbor)
        allValues.append(currentValue)
        if currentValue < solution.value:
            solution.setState(nextNeighbor)
            allBestValues.append(currentValue)
            currentState = nextNeighbor
        else:
            allBestValues.append(solution.value)
        iterations += 1

    output = {
        "solution": solution.value,
        "allValues": allValues,
        "allBestValues": allBestValues
    }
    return output


def randomRestartHillClimbing(problem, execution):
    iterations = 0
    solution = Solution(problem, execution)
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
            solution.setState(nextNeighbor)
            allBestValues.append(currentValue)
            currentState = nextNeighbor
        else:
            allBestValues.append(solution.value)
        iterations += 1

    output = {
        "solution": solution.value,
        "allValues": allValues,
        "allBestValues": allBestValues
    }
    return output


def simulatedAnneling(problem, execution):
    iterations = 0
    solution = Solution(problem, execution)
    currentState = solution.state
    temperature = 1

    allValues = []
    allBestValues = []
    bestValue = float("inf")

    while iterations < 1000:
        nextNeighbor = problem.getNextNeighbor(currentState)
        currentValue = problem.objectiveFunction(nextNeighbor)
        allValues.append(currentValue)
        if currentValue < bestValue:
            bestValue = currentValue
        allBestValues.append(bestValue)
        if currentValue < solution.value:
            solution.setState(nextNeighbor)
            currentState = nextNeighbor
        else:
            if round(random.random(), 5) < temperature:
                solution.setState(nextNeighbor)
                currentState = nextNeighbor

        iterations += 1
        temperature = cooling(temperature, 900)

    output = {
        "solution": bestValue,
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


def geneticAlgorithm(problem, execution):
    populationSize = 20
    generations = 50
    population = []

    allValues =[]

    population.append(Solution(problem, execution))
    for individual in range(populationSize - 1):
        population.append(Solution(problem, -1))

    for generation in range(generations):
        currentPopulation = []

        for individual in range(0, populationSize, 2):
            parents = chooseParents(population)
            childrenStates = problem.crossover(parents)
            currentPopulation.append(
                Solution(
                    problem, execution, problem.mutation(childrenStates[0])
                )
            )
            currentPopulation.append(
                Solution(
                    problem, execution, problem.mutation(childrenStates[1])
                )
            )

        population = currentPopulation
        for solution in currentPopulation:
            allValues.append(solution.value)

    output = {
        "solution": reduce(
            (lambda x, y: x if x < y else y),
            allValues
        ),
        "allValues": allValues,
        "allBestValues": findBestValues(allValues)
    }

    return output


def findBestValues(allValues):
    allBestValues = []
    currentBest = float("inf")
    for value in allValues:
        if value < currentBest:
            currentBest = value
        allBestValues.append(currentBest)

    return allBestValues


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
