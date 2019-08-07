
import pandas as pd
import os
from collections import OrderedDict

#CHUNK_SIZE = 4000 #usual file system block size 4KB
#CHUNK_SIZE = 6400000 #usual hadoop chunk size 64MB
CHUNK_SIZE = 256000 #256kB Chunk Size as reported in LCN Paper
stat_file_name = "chunk.csv"
directory_name = "." #current directory

def main():
    print("Generating chunk popularity statistics ")

    if os.path.exists(stat_file_name):
        os.remove(stat_file_name)

    list_of_all_files = os.listdir(directory_name)
    intensity_dict = dict()

    for file in list_of_all_files:
        if not file.endswith(".csv"):
            continue
        df = pd.read_csv(file, names=["timestamp", "CPU_ID", "process", "action",
                                                                       "operation", "sector", "size"])
        minimum = df['sector'].min()
        maximum = df['sector'].max()
        df = df.dropna(subset=['sector'])

        for index, row in df.iterrows():
            second_val = int(row['sector'])
            second_val = int(second_val / CHUNK_SIZE)
            if second_val not in intensity_dict:
                intensity_dict[second_val] = row['size']
            else:
                intensity_dict[second_val] += row['size']
        print ("Finished parsing "+ str(file))

    fp = open(stat_file_name, "w")
    time = list()
    intensity = list()
    intensity_dict = OrderedDict(sorted(intensity_dict.items(), key=lambda x: x[1], reverse=True))
    count = 0
    for key in intensity_dict:
        count = count +1
        time.append(count)
        intensity.append(intensity_dict[key])
        fp.write(str(key)+","+str(intensity_dict[key])+"\n")

    fp.close()

if __name__ == '__main__':
    main()