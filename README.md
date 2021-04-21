# Demonstrating Coverage + Spark

This is a short example of how to run Pyspark locally and get coverage data from it.

This uses poetry for installation. On macOS, a homebrew installation of the `apache-spark` package is needed. Follow the homebrew instructions to make sure that `openjdk@11` is in your path first.

```bash
$ brew install apache-spark
$ poetry install   # installs pyspark, coverage, and findspark
$ poetry run 
```

## How it works

The `findspark` module is used when run locally to instantiate the `SparkSession` that is designed to run locally on the calling machine, as opposed to `spark-submit`.

Because it runs locally, `coverage` will be aware of the execution path for the code and will be able to produce a report as normal.

We separate `main.py` from the functions for testability and to allow for distinct creation/finding of the `SparkSession`.

## Other notes

Obviously, I didn't worry about errors or good parsing of arguments, etc., etc.