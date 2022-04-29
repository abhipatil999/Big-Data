**Pre-requisite

In your shell after installing PySpark first import packages:
Go to your python shell & execute the following in terminal

pip install findspark

import findspark
findspark.init()

(import the necessary modules)

from pyspark import SparkContext
from pyspark import SparkConf

Done!!


For a Spark execution in pyspark two components are required to work together:

pyspark python package
Spark instance in a JVM

When launching things with spark-submit or pyspark, these scripts will take care of both, i.e. they set up your PYTHONPATH, PATH, etc,
so that your script can find pyspark, and they also start the spark instance, configuring according to your params, e.g. --master X