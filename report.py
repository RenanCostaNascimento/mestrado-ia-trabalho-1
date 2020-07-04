from numpy import max, min, mean, std
from charts import plotChart


def generateComparisonTable(algorithm, results):
    allBestValues = []
    for result in results:
        allBestValues.append(result.get("solution"))

    print("-----", algorithm, "-----")
    print("Melhores Valores\n", allBestValues)
    print("Max", max(allBestValues))
    print("Min", min(allBestValues))
    print("Mean", mean(allBestValues))
    print("Std", std(allBestValues))
    print("\n")


def generateFitnessEvolutionChart(algorithm, results):

    yAxis = []
    for result in results:
        yAxis.append(result.get("allBestValues"))

    title = "Fitness Evolution Chart ({algorithm})".format(algorithm=algorithm)
    legend = {
        "title": "Executions",
        "labels": ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º", "10º"]
    }

    plotChart(yAxis, title, legend)
