from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder.appName("AirlineDelayAnalysis").getOrCreate()

def load_data(spark, path):
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df