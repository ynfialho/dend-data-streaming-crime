# SF Crime Statistics with Spark Streaming

## Pre requirements
* Python 3.7+
* Apache Spark 3.0.1
* Apache Kafka(standalone)

## Run

**1- Producer Python**
```shell
python3 kafka_server.py
```

**2- Consumer Python**
```shell
python3 consumer_server.py
```

**2- Consumer Spark Streaming**
```shell
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 --master local[*] data_stream.py
```

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