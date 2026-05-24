from src.data_loader import create_spark_session, load_data
from src.data_cleaning import clean_data, check_nulls
from src.analysis import (
    time_based_analysis,
    carrier_analysis,
    carrier_delay_causes,
    airport_analysis,
    delay_causes_analysis,
    monthly_delay_analysis
)
from src.visualization import plot_all

def main():
    spark = create_spark_session()

    df = load_data(spark, "data/raw/Airline_Delay_Cause.csv")

    print("Checking null values...")
    check_nulls(df).show()

    df = clean_data(df)

    print("Running analysis...")

    time_df = time_based_analysis(df)
    carrier_df = carrier_analysis(df)
    carrier_caused_df = carrier_delay_causes(df)
    airport_df = airport_analysis(df)
    year_causes_df, month_causes_df = delay_causes_analysis(df)
    month_delay_df = monthly_delay_analysis(df)

    print("Generating visualizations...")
    plot_all(time_df, carrier_df, carrier_caused_df, airport_df,
             year_causes_df, month_causes_df, month_delay_df)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()