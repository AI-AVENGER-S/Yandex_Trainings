import matplotlib.pyplot as plt
import pandas as pd


def statistics(title, color, data):
    plt.figure()
    names = list(data.keys())
    values = list(data.values())
    students = pd.DataFrame(data)
    plt.hist(students["math score"], label=title)

    plt.legend()
    plt.show()

    plt.savefig("result.png")
    plt.close()
