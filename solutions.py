import random
import numpy as np


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
    mutationChance = 0.3
    population = []

    for individual in range(populationSize):
        population.append(Solution(problem))

    for generation in range(generations):
        currentPopulation = []

        for individual in range(0, populationSize, 2):
            parents = chooseParents(population)
            states = problem.crossover(parents)
            currentPopulation.append(
                mutation(Solution(problem, states[0]), mutationChance))
            currentPopulation.append(
                mutation(Solution(problem, states[1]), mutationChance))

        population = currentPopulation
        print("geracao ", generation + 1)
        for i in population:
            print(i)

    return population


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


def mutation(individual, mutationChance):
    if random.random() > mutationChance:
        individual.setState(individual.state + np.random.normal(0.0, 0.1))

    return individual


# testCooling(90, 100)
# print()
