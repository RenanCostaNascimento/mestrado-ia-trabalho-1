import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotChart(data, title, legend):
    sns.set(style="whitegrid")

    dataset = {
        "xAxis": list(range(1, 1001))
    }
    for index in range(0, len(data)):
        dataset[str(index + 1) + "º"] = data[index]
    dataFrame = pd.DataFrame(dataset)

    axis = sns.lineplot(
        x='xAxis', y='value', hue='variable', legend=False, ci="sd",
        data=pd.melt(dataFrame, ['xAxis'])
    )
    axis.set(xlabel='Objective Function Calls',
             ylabel='Objective Function Value')
    axis.set_title(title)
    axis.set(xlim=(0, 1000))
    plt.legend(title=legend["title"],
               loc='upper right', labels=legend["labels"])

    plt.show()
