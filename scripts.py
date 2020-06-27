from charts import plotChart
from problems import Problem1
from solutions import hillClimbing, randomRestartHillClimbing, simulatedAnneling, geneticAlgorithm


def runProblem1():
    problem1 = Problem1()
    # hillClimbingOutput = randomRestartHillClimbing(problem1)
    # simulatedAnnelingOutput = simulatedAnneling(problem1)

    # x = list(range(1, 1001))
    # y = simulatedAnnelingOutput.get("allValues")


    geneticAlgorithmOutput = geneticAlgorithm(problem1)
    x = list(range(1, 51))
    y = geneticAlgorithmOutput

    plotChart(x, y)

runProblem1()