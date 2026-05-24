import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_all(time_df, carrier_df, carrier_caused_df, airport_df, year_causes_df, month_causes_df, month_delay_df):

    pd_time = time_df.toPandas().sort_values(["year", "month"])
    pd_time['date'] = pd.to_datetime(pd_time[['year', 'month']].assign(day=1))

    pd_carrier = carrier_df.limit(10).toPandas()
    pd_carrier_caused = carrier_caused_df.limit(10).toPandas()
    pd_airport = airport_df.limit(10).toPandas()

    causes = ["carrier_ct", "weather_ct", "nas_ct", "security_ct", "late_aircraft_ct"]

    pd_year_causes = year_causes_df.toPandas().set_index('year').sort_index()
    pd_year_causes_pct = pd_year_causes.div(pd_year_causes.sum(axis=1), axis=0) * 100

    pd_month_causes = month_causes_df.toPandas()
    pd_month_delay = month_delay_df.toPandas()

    plt.figure(figsize=(15, 20))

    plt.subplot(4, 2, 1)
    plt.plot(pd_time['date'], pd_time['delay_rate'])
    plt.title("Flight Delay Rate Over Time")

    plt.subplot(4, 2, 2)
    sns.barplot(data=pd_carrier, x='avg_delay_rate', y='carrier_name')
    plt.title("Top 10 Airlines by Delay Rate")

    plt.subplot(4, 2, 3)
    sns.barplot(data=pd_carrier_caused, x='total_carrier_ct', y='carrier_name')
    plt.title("Carrier-Caused Delays")

    plt.subplot(4, 2, 4)
    sns.barplot(data=pd_airport, x='delay_rate', y='airport')
    plt.title("Top Airports by Delay Rate")

    plt.subplot(4, 2, 5)
    pd_year_causes_pct.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title("Delay Causes by Year (%)")

    plt.subplot(4, 2, 6)
    for cause in causes:
        plt.plot(pd_month_causes['month'], pd_month_causes[cause], label=cause)
    plt.legend()
    plt.title("Monthly Delay Causes")

    plt.subplot(4, 2, 7)
    plt.plot(pd_month_delay['month'], pd_month_delay['delay_rate'], marker='o')
    plt.title("Monthly Delay Rate")

    plt.tight_layout()
    plt.savefig("outputs/plots/all_visualizations.png")
    plt.show()