from charts import plotChart
from problems import Problem1, Problem2, Problem3
from solutions import hillClimbing, randomRestartHillClimbing, simulatedAnneling, geneticAlgorithm
from report import generateComparisonTable, generateFitnessEvolutionChart, generateAlgorithmComparisonChart, generateAllValuesChart


def solveProblem(problem):
    hillClimbingResults = []
    randomRestartHillClimbingResults = []
    simulatedAnnelingResults = []
    geneticAlgorithmResults = []
    algorithmNames = [
        "Hill Climbing", "Random Restart Hill Climbing",
        "Simulated Anneling", "Genetic Algorithm"
    ]

    for execution in range(10):
        hillClimbingResults.append(hillClimbing(problem))
        randomRestartHillClimbingResults.append(randomRestartHillClimbing(problem))
        simulatedAnnelingResults.append(simulatedAnneling(problem))
        geneticAlgorithmResults.append(geneticAlgorithm(problem))

    # Comparison Table
    generateComparisonTable(algorithmNames[0], hillClimbingResults)
    generateComparisonTable(algorithmNames[1], randomRestartHillClimbingResults)
    generateComparisonTable(algorithmNames[2], simulatedAnnelingResults)
    generateComparisonTable(algorithmNames[3], geneticAlgorithmResults)

    # All Values Chart (Optional)
    generateAllValuesChart(algorithmNames[0], hillClimbingResults[0])
    generateAllValuesChart(algorithmNames[1], randomRestartHillClimbingResults[0])
    generateAllValuesChart(algorithmNames[2], simulatedAnnelingResults[0])
    generateAllValuesChart(algorithmNames[3], geneticAlgorithmResults[0])

    # Fitness Evolution Chart
    generateFitnessEvolutionChart(algorithmNames[0], hillClimbingResults)
    generateFitnessEvolutionChart(algorithmNames[1], randomRestartHillClimbingResults)
    generateFitnessEvolutionChart(algorithmNames[2], simulatedAnnelingResults)
    generateFitnessEvolutionChart(algorithmNames[3], geneticAlgorithmResults)

    # Algorithm Comparison Chart
    generateAlgorithmComparisonChart(
        algorithmNames,
        [hillClimbingResults, randomRestartHillClimbingResults, simulatedAnnelingResults, geneticAlgorithmResults]
    )


def startProblem(userInput):
    if userInput == "1":
        return Problem1()

    if userInput == "2":
        return Problem2()

    if userInput == "3":
        return startProblem3()

    return None


def userInterface():
    print("Which Problem would you like to solve?\n- 1\n- 2\n- 3")
    userInput = input()
    problem = startProblem(userInput)
    if problem:
        print("\nSure! I'll show you all the charts (images) and tables (prompt) of the Problem {problem}".format(
            problem=userInput))
        print("Once you close a chart the next one will be displayed, ok?\n")
        solveProblem(problem)
    else:
        print("You have to choose a number man...")


def startProblem3():
    # citiesFile = open("tsp-example-5cities.txt")
    # citiesFile = open("tsp-example-10cities.txt")
    citiesFile = open("tsp-example-rwanda-1621cities.txt")
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

    return Problem3(cities)


userInterface()
