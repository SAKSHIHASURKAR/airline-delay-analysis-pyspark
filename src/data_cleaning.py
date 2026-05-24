from pyspark.sql import functions as F

def check_nulls(df):
    null_counts = df.select([
        F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns
    ])
    return null_counts

def clean_data(df):
    df = df.fillna(0)
    df = df.filter(F.col("arr_flights") > 0)
    return df