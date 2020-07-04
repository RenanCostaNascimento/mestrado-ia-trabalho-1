from charts import plotChart
from problems import Problem1, Problem2, Problem3
from solutions import hillClimbing, randomRestartHillClimbing, simulatedAnneling, geneticAlgorithm
from report import generateComparisonTable, generateFitnessEvolutionChart


def runProblem1():
    problem1 = Problem1()
    hillClimbingResults = []
    randomRestartHillClimbingResults = []
    simulatedAnnelingResults = []
    geneticAlgorithmResults = []
    algorithmNames = [
        "Hill Climbing", "Random Restart Hill Climbing",
        "Simulated Anneling", "Genetic Algorithm"
    ]

    for execution in range(10):
        hillClimbingResults.append(hillClimbing(problem1))
        randomRestartHillClimbingResults.append(randomRestartHillClimbing(problem1))
        simulatedAnnelingResults.append(simulatedAnneling(problem1))
        geneticAlgorithmResults.append(geneticAlgorithm(problem1))

    # Comparison Table
    generateComparisonTable(algorithmNames[0], hillClimbingResults)
    generateComparisonTable(algorithmNames[1], randomRestartHillClimbingResults)
    generateComparisonTable(algorithmNames[2], simulatedAnnelingResults)
    generateComparisonTable(algorithmNames[3], geneticAlgorithmResults)

    # Fitness Evolution Chart
    generateFitnessEvolutionChart(algorithmNames[0], hillClimbingResults)
    generateFitnessEvolutionChart(algorithmNames[1], randomRestartHillClimbingResults)
    generateFitnessEvolutionChart(algorithmNames[2], simulatedAnnelingResults)
    generateFitnessEvolutionChart(algorithmNames[3], geneticAlgorithmResults)

    # x = list(range(1, 1001))
    # y = hillClimbingOutput.get("allBestValues")

    # x = list(range(1, 51))
    # y = geneticAlgorithmOutput.get("allValues")

    # print("ALL", geneticAlgorithmOutput.get("allValues"))
    # print("BEST", geneticAlgorithmOutput.get("solution"))

    # plotChart(x, y)


runProblem1()


def runProblem2():
    problem2 = Problem2()
    # hillClimbingOutput = hillClimbing(problem2)
    # randomRestartHillClimbingOutput = randomRestartHillClimbing(problem2)
    simulatedAnnelingOutput = simulatedAnneling(problem2)
    # geneticAlgorithmOutput = geneticAlgorithm(problem2)

    x = list(range(1, 1001))
    y = simulatedAnnelingOutput.get("allValues")

    # geneticAlgorithmOutput = geneticAlgorithm(problem2)
    # x = list(range(1, 51))
    # y = geneticAlgorithmOutput

    plotChart(x, y)

# runProblem2()


def runProblem3():
    # citiesFile = open("tsp-example-5cities.txt")
    citiesFile = open("tsp-example-10cities.txt")
    # citiesFile = open("tsp-example-10cities-solution.txt")
    # citiesFile = open("tsp-example-rwanda-1621cities.txt")
    cities = []
    lineNumber = 0
    for line in citiesFile:
        splittedText = line.strip().split()
        lineNumber += 1
        coordinates = {
            "city": lineNumber,
            "x": float(splittedText[0]),
            "y": float(splittedText[1]),
        }
        cities.append(coordinates)
    citiesFile.close()
    problem3 = Problem3(cities)

    # hillClimbingOutput = hillClimbing(problem3)
    # randomRestartHillClimbingOutput = randomRestartHillClimbing(problem3)
    # simulatedAnnelingOutput = simulatedAnneling(problem3)
    # geneticAlgorithmOutput = geneticAlgorithm(problem2)

    # x = list(range(1, 1001))
    # y = hillClimbingOutput.get("allBestValues")
    # print(hillClimbingOutput.get("solution").value)

    # geneticAlgorithmOutput = geneticAlgorithm(problem2)
    # x = list(range(1, 51))
    # y = geneticAlgorithmOutput

    # plotChart(x, y)


# runProblem3()
