# TempleTraceAnalysis
Used this python script to generate the statistics from the Temple University Traces. I used this statistics for one of our work titled "Adaptive Data Center Network Traffic Management for Distributed High Speed Storage" published in LCN 2019

You can get the direct access link of temple traces from the paper mentioned above. Due to copyright issue I can't upload it here.

Once you get the traces, do the following:

1) Run the **chunk_statistics.py** file. Before running, make sure you have changed the **stat_file_name, directory_name** variables. It's up to you whether you change the value of **CHUNK_SIZE**

2)After **chunk_statistics.py** finished, run **plot_chunk_statistics.py** to generate the plot, which mainly shows the characteristics of the popularity of data chunks. 
