# SF Crime Statistics with Spark Streaming

## Questions

#### 1- How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
It either increased or decreased **processedRowsPerSecond**.

#### 2- What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
The properties that showed variations were:
```python
.config("maxOffsetsPerTrigger", 200) \
.config("spark.default.parallelism", 50) \
.config("spark.sql.shuffle.partitions", 100) \
```