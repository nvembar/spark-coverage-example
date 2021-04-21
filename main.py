import sys
import spark_functions as sf


if __name__ == "__main__":
    # This indicates that this is a local (not spark-submit) execution
    local = len(sys.argv) >= 2 and sys.argv[1] == "--local"

    if local:
        # Load up findspark
        import findspark

        findspark.init()

    from pyspark import SparkConf
    from pyspark.sql import SparkSession

    spark = None

    if local:
        spark_conf = (
            SparkConf()
            .setMaster("local[2]")
            .setAppName("run-job-local")
            .set(
                # This allows JDK 11 to work locally - set this on EMR/cluster
                # in the distributed environment
                "spark.driver.extraJavaOptions",
                "-Dio.netty.tryReflectionSetAccessible=true",
            )
            .set(
                "spark.executor.extraJavaOptions",
                "-Dio.netty.tryReflectionSetAccessible=true",
            )
        )
        spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    else:
        spark = SparkSession.builder.getOrCreate()

    sf.function_that_runs(spark)
