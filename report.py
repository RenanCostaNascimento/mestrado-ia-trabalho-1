from numpy import max, min, mean, std

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



