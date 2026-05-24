
# Airline Delay Analysis

A PySpark-powered big data analytics project that explores U.S. airline delay patterns, identifies major delay causes, and visualises airline and airport performance trends over time.


## Overview
Airline delays are a significant challenge in the aviation industry, affecting millions of passengers and costing airlines billions of dollars annually. Delays can occur due to operational inefficiencies, adverse weather conditions, air traffic congestion, security issues, or delays propagated from previous flights.

This project analyses the U.S. Bureau of Transportation Statistics Airline Delay Cause dataset using Apache Spark (PySpark) for scalable distributed processing and Python visualisation libraries for exploratory data analysis.

The project focuses on:

Identifying airlines with the highest delay rates
Analysing airport-level delay patterns
Understanding seasonal delay trends
Investigating dominant causes of delays
Visualising yearly and monthly delay behaviour

The analysis provides meaningful insights into how operational inefficiencies and external factors contribute to airline delays across the United States.

## Problem Statement
Flight delays negatively impact:

Passenger satisfaction
Airline operational costs
Airport efficiency
Fuel consumption
Crew scheduling
Overall transportation reliability

Despite the availability of airline operational data, delay causes are rarely analysed holistically using scalable big data tools.

This project aims to answer the following questions:

Which airlines experience the highest delay rates?
Which airports are most affected by delays?
How do delays vary across months and years?
Which delay causes dominate overall?
How significant is the impact of weather compared to operational inefficiencies?
Are airline delays improving or worsening over time?

## Dataset
Dataset Source

Bureau of Transportation Statistics (BTS)

Dataset Name

Airline_Delay_Cause.csv

Dataset Description

The dataset contains detailed airline arrival and delay statistics collected from U.S. airlines.

Dataset Features
| Column Name        | Description                             |
| ------------------ | --------------------------------------- |
| `year`             | Year of observation                     |
| `month`            | Month of observation                    |
| `carrier_name`     | Airline carrier name                    |
| `airport`          | Airport IATA airport code               |
| `arr_flights`      | Total arriving flights                  |
| `arr_del15`        | Flights delayed more than 15 minutes    |
| `carrier_ct`       | Carrier-caused delay count              |
| `weather_ct`       | Weather-caused delay count              |
| `nas_ct`           | National Airspace System delay count    |
| `security_ct`      | Security-related delay count            |
| `late_aircraft_ct` | Delays caused by late incoming aircraft |

Dataset Size

•	Format: CSV 

•	Records: ~500,000+ rows 

•	Type: Structured tabular dataset

## Tools and Technologies
| Tool / Technology | Purpose                             |
| ----------------- | ----------------------------------- |
| **PySpark**       | Distributed data processing         |
| **Spark SQL**     | Data aggregation and transformation |
| **Pandas**        | Data manipulation for plotting      |
| **Matplotlib**    | Data visualisation                  |
| **Seaborn**       | Statistical visualisation           |
| **Google Colab**  | Cloud notebook environment          |
| **Python**        | Programming language                |
| **NumPy**         | Numerical operations                |

## Methods
The project follows a structured data analytics workflow:

Data Ingestion

•	Loaded the CSV dataset into a Spark DataFrame  

•	Used schema inference for automatic datatype detection

Data Cleaning

•	Audited missing values across all columns 

•	Replaced null numeric values with 0 

•	Removed records where arr_flights = 0 

•	Ensured data consistency before analysis

Feature Engineering

A new feature called Delay Rate was created:

delay_rate=(arr_del15)/(arr_flights)

This metric allows fair comparison across airlines and airports regardless of flight volume.

Aggregation and Analysis

Performed multiple aggregations using PySpark:

•	Monthly delay trend analysis 

•	Airline-wise delay analysis 

•	Airport-wise delay analysis 

•	Delay cause distribution analysis 

•	Seasonal pattern analysis

Cause Analysis

Analysed five major delay categories:

•	Carrier delays 

•	Weather delays 

•	NAS delays 

•	Security delays 

•	Late aircraft delays 

Computed:

•	Total yearly contribution 

•	Monthly seasonal variations 

•	Percentage distribution by year

Visualisation

Generated multiple visualisations using Matplotlib and Seaborn:

•	Line charts 

•	Horizontal bar charts 

•	Stacked bar charts 

•	Multi-line seasonal trend charts


## Key Insights
Seasonal Delay Peaks

Flight delays consistently increase during:

•	Summer travel season (June – July) 

•	Holiday season (December)

Carrier Inefficiencies

A small number of airlines contribute disproportionately to carrier-caused delays due to:

•	Scheduling inefficiencies 

•	Aircraft turnaround delays 

•	Operational bottlenecks

Late Aircraft Propagation Dominates

Late aircraft delays are the largest contributor overall, indicating:

•	Tight scheduling systems 

•	Lack of operational buffer time 

•	Cascading delay effects 

Weather Delays are Seasonal

Weather-related delays peak during:

•	Winter storms 

•	Summer thunderstorms 

However, weather contributes less annually compared to operational inefficiencies.

Airport Bottlenecks

Several smaller regional airports show higher delay rates than major hub airports due to:

Limited infrastructure

Reduced operational flexibility

Weather sensitivity


## Dashboard / Output / Model 
The project generates several analytical visualisations:
| # | Visualisation                  | Description                               |
| - | ------------------------------ | ----------------------------------------- |
| 1 | Flight Delay Rate Over Time    | Monthly delay trends                      |
| 2 | Top Airlines by Delay Rate     | Airline performance ranking               |
| 3 | Carrier-Caused Delay Counts    | Airline operational inefficiency analysis |
| 4 | Top Airports by Delay Rate     | Airport performance analysis              |
| 5 | Delay Cause Breakdown by Year  | Percentage contribution of causes         |
| 6 | Seasonal Delay Causes by Month | Monthly cause-wise trends                 |
| 7 | Monthly Delay Seasonality      | Delay rate seasonal analysis              |

Output Generated :

•	Visual analytics dashboard 

•	Airline rankings 

•	Airport rankings 

•	Delay cause analysis

#  How to Run This Project

## Option 1 — Local Environment

### Step 1 — Clone the Repository
```bash
git clone https://github.com/<your-username>/airline-delay-analysis.git
cd airline-delay-analysis
```

---

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4 — Add Dataset

Place the dataset inside the `data/` folder:

```
project-root/
│── data/
│    └── Airline_Delay_Cause.csv
```

If needed:

```bash
cp /your/path/Airline_Delay_Cause.csv data/
```

---

### Step 5 — Run the Project

Run the main pipeline:

```bash
python main.py
```

---

### Step 6 — View Outputs

After execution, results will be saved in:

- `outputs/plots/` → Visualizations
- `outputs/` → Reports / processed results

---

## Option 2 — Run Individual Modules (For Debugging)

```bash
python src/data_loader.py
python src/data_cleaning.py
python src/analysis.py
python src/visualization.py
```

---

## Project Structure

```
airline-delay-analysis/
│── data/
│    └── Airline_Delay_Cause.csv
│── src/
│    ├── data_loader.py
│    ├── data_cleaning.py
│    ├── analysis.py
│    ├── visualization.py
│    └── main.py
│── outputs/
│── requirements.txt
│── README.md
```

---

## Notes

- Always run `main.py` for full pipeline execution
- Ensure all dependencies are installed before running
- Use virtual environment for best results

## Results and Conclusion

The analysis demonstrates that airline delays are driven primarily by :

•	Late aircraft propagation 

•	Carrier-side inefficiencies

•	Seasonal congestion patterns 

Major Findings

•	Late aircraft delays consistently dominate across all years 

•	Summer and holiday months experience the highest delays 

•	Operational inefficiencies contribute more than weather annually 

•	Smaller airports often experience unexpectedly high delay rates 

Conclusion :

The project successfully demonstrates the power of PySpark for large-scale transportation analytics and highlights how data-driven insights can support:

•	Airline scheduling optimisation 

•	Airport infrastructure planning 

•	Improved passenger experience


## Future Work 
Possible future improvements include :

•	Machine learning models for delay prediction 

•	Real-time streaming analysis using Spark Streaming 

•	Interactive dashboards using Plotly or Tableau 

•	Weather API integration 

•	Flight route network analysis 

•	Airport clustering and segmentation 

•	Predictive analytics for operational planning


## Author and Contact 
Author

*Sakshi Ashok Hasurkar*  
AI & Data Analytics Enthusiast | Master's Student in Artificial Intelligence  

I am a Computer Engineer with experience in software testing and a strong interest in data analytics and machine learning. Currently pursuing a Master's in Artificial Intelligence at the University of East London, I am focused on building data-driven solutions and scalable analytics projects using tools like PySpark and Python.

- Master's in Artificial Intelligence – University of East London  
- 1+ year experience as Software Tester (NHS UK Project)  
- Skills: Python, PySpark, Data Analysis, Machine Learning  
-London, UK  

### Connect with Me
- LinkedIn: www.linkedin.com/in/sakshi-hasurkar-57b2412bb