# TempleTraceAnalysis
Used this python script to generate the statistics from the Temple University Traces. I used this statistics for one of our work titled "Adaptive Data Center Network Traffic Management for Distributed High Speed Storage" published in LCN 2019

You can get the direct access link of temple traces from the paper mentioned above. Due to copyright issue I can't upload it here.

Once you have your hand on the traces, do the following:

1) Run the **chunk_statistics.py** file. Before running, make sure you have changed the **stat_file_name, directory_name** variables. It's up to you whether you change the value of **CHUNK_SIZE**

2) After **chunk_statistics.py** finished, run **plot_chunk_statistics.py** to generate the plot, which mainly shows the characteristics of the popularity of data chunks. Make sure, value of **stat_file_name** variable of this file is same as the **stat_file_name** of the **chunk_statistics.py** file.

We generate the plots on a day basis. For example to generate the statitics for the 13th March storages accesses, we copy contents of all the three folders (2019_03_13_p1,2019_03_13_p2,2019_03_13_p3) presenting different application storage access on March 13,2019, put altogether in a folder and point it by **directory_name** variable.
