import random

from pyspark.sql import DataFrame, Row
import pyspark.sql.functions as F


def function_that_runs(spark):
    rows = [
        Row(row_no=i, value=random.uniform(1.0, 2000.0)) for i in range(1000)
    ]
    df = spark.createDataFrame(rows)
    averaged = df.agg(F.avg(F.col("value")).alias("random_average"))
    averaged.show()
    print("This runs!!")


def function_that_doesnt_run(spark):
    print("This shouldn't!!")

