import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotChart(x, y):
    sns.set()
    plt.plot(x, y)
    plt.legend('ABCDEF', ncol=2, loc='upper right')
    plt.show()
