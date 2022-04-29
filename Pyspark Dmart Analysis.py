import findspark
findspark.init('/home/jubinsoni/spark-2.1.0-bin-hadoop2.7')
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Dmart').getOrCreate()
df = spark.read.csv('dmart_stock.csv', inferSchema=True, header=True)
df.columns
df.printSchema()
for line in df.head(5):
 print(line, '\n')