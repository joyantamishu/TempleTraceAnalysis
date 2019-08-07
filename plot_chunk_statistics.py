
import pandas as pd
import os
from collections import OrderedDict
import matplotlib.pyplot as plt

stat_file_name = "chunk.csv"

def main():
    print("Temple Trace Analysis")

    df = pd.read_csv(stat_file_name, names=["chunk", "popularity"])
    time = list()
    intensity = list()
    count = 0
    for index, row in df.iterrows():
        #print(row["popularity"])
        count = count + 1
        time.append(count)
        intensity.append(row["popularity"]+ 10)

    intensity = [float(i) / sum(intensity) for i in intensity]
    intensity_relative = [float(i) / max(intensity) for i in intensity]
    intensity_sum = list()

    sum_total = 0
    for single in intensity:
        intensity_sum.append(sum_total)
        sum_total = sum_total + single
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.plot(time, intensity_relative, label='Relative Popularity')
    plt.plot(time, intensity_sum, label = "CDF of Popularity")
    plt.legend(loc='center right', prop={'size': 14})
    plt.xlabel('Chunk Index (sorted by Popularity)',  fontsize=14)
    plt.ylabel('Popularity (Byte Accessed)', fontsize=14)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()