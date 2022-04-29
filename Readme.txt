**Pre-requisite

In your shell after installing PySpark first import packages:
Go to your python shell & execute the following in terminal

#pip install findspark

#import findspark
#findspark.init()

(import the necessary modules)

#from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

**To set PySpark environment variables, first, 
get the PySpark installation direction path by running the Python command

 #pip show pyspark

Now set the SPARK_HOME & PYTHONPATH according to your installation

export SPARK_HOME=/Users/prabha/apps/spark-2.4.0-bin-hadoop2.7
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH


Done!!


