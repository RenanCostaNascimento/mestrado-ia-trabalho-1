import numpy as np
from charts import plotChart, plotComparisonChart


def generateComparisonTable(algorithm, results):
    allBestValues = []
    for result in results:
        allBestValues.append(result.get("solution"))

    print("-----", algorithm, "-----")
    print("Melhores Valores\n", allBestValues)
    print("Max", max(allBestValues))
    print("Min", min(allBestValues))
    print("Mean", np.mean(allBestValues))
    print("Std", np.std(allBestValues))
    print("\n")


def generateFitnessEvolutionChart(algorithm, results):

    yAxis = []
    for result in results:
        yAxis.append(result.get("allBestValues"))

    title = "Fitness Evolution ({algorithm})".format(algorithm=algorithm)
    legend = {
        "title": "Executions",
        "labels": ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º", "10º"]
    }

    plotChart(yAxis, title, legend)


def generateAlgorithmComparisonChart(algorithmNames, algorithmResults):

    yAxis = []
    currentResults = []
    for algorithm in algorithmResults:
        currentResults.clear()
        for result in algorithm:
            currentResults.append(result.get("allBestValues"))
        yAxis.append({
            "mean": np.mean(currentResults, axis=0),
            "std": np.std(currentResults, axis=0)
        })

    title = "Algorithm Comparison (Mean)"
    legend = {
        "title": "Algorithms",
        "labels": algorithmNames
    }

    plotComparisonChart(yAxis, title, legend)


def generateAllValuesChart(algorithm, result):
    title = "All Values ({algorithm})".format(algorithm=algorithm)
    legend = {
        "title": "Result",
        "labels": ["1º"]
    }

    plotChart([result.get("allValues")], title, legend)
