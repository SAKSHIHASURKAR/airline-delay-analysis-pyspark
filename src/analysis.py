from pyspark.sql import functions as F

def time_based_analysis(df):
    return df.groupBy("year", "month").agg(
        F.sum("arr_del15").alias("total_delays"),
        F.sum("arr_flights").alias("total_flights")
    ).withColumn("delay_rate", F.col("total_delays") / F.col("total_flights"))

def carrier_analysis(df):
    return df.groupBy("carrier_name").agg(
        F.sum("arr_del15").alias("total_delays"),
        F.sum("arr_flights").alias("total_flights")
    ).withColumn("avg_delay_rate", F.col("total_delays") / F.col("total_flights")) \
     .orderBy(F.desc("avg_delay_rate"))

def carrier_delay_causes(df):
    return df.groupBy("carrier_name").agg(
        F.sum("carrier_ct").alias("total_carrier_ct")
    ).orderBy(F.desc("total_carrier_ct"))

def airport_analysis(df):
    return df.groupBy("airport").agg(
        F.sum("arr_del15").alias("total_delays"),
        F.sum("arr_flights").alias("total_flights")
    ).withColumn("delay_rate", F.col("total_delays") / F.col("total_flights")) \
     .orderBy(F.desc("delay_rate"))

def delay_causes_analysis(df):
    causes = ["carrier_ct", "weather_ct", "nas_ct", "security_ct", "late_aircraft_ct"]
    
    year_causes = df.groupBy("year").agg(*[
        F.sum(c).alias(c) for c in causes
    ])
    
    month_causes = df.groupBy("month").agg(*[
        F.sum(c).alias(c) for c in causes
    ]).orderBy("month")
    
    return year_causes, month_causes

def monthly_delay_analysis(df):
    return df.groupBy("month").agg(
        F.sum("arr_del15").alias("total_delays"),
        F.sum("arr_flights").alias("total_flights")
    ).withColumn("delay_rate", F.col("total_delays") / F.col("total_flights")) \
     .orderBy("month")