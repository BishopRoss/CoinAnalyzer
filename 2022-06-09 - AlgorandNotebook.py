# Databricks notebook source
# MAGIC %md # Workbook for data obtained on the Algorand currency 

# COMMAND ----------

# Where the first data frame was initialized from the CSV file I had imported into the notebook directory. 
# After importing the file and creating the dataframe with pyspark, manipulatable graphs/charts can be created to view and represent the historical data present in the dataframe
# This dataframe in particular is set to display the closing prices for the Algorand currency from the 1st of January to the 9th of June. 

# File location and type
file_location = "/FileStore/tables/AlgorandReport.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)



display(df)

# COMMAND ----------

# Creates a second dataframe from the same data contained in the CSV report file
# This dataframe in particular is set to display the volume of the Algorand currency that was traded from the 1st of January to the 9th of June. 
# File location and type
file_location = "/FileStore/tables/AlgorandReport.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

# The cluster the notebook is attached to is initialized with the "cbpro" library. The cbpro library is coinbase pro's API endpoint so that data can be retrieved from the Coinbase exchange for furhter 
# analysis. 
# To represent the result set returned from Coinbase, the "pandas" library is utilized so the data that will be inserted into the CSV file can be reviewed beforehand
import cbpro
import pandas as pd

b = cbpro.PublicClient()
pd.set_option('display.max_rows',None)
# On line 11 below is where the date ranges can be specified. 
historical = pd.DataFrame(
    b.get_product_historic_rates(product_id="ALGO-USD", start="2022-4-30", end="2022-6-10", granularity=21600))
historical.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
historical['Date'] = pd.to_datetime(historical['Date'], unit='s')
historical.set_index('Date', inplace=True)
historical.sort_values(by='Date', ascending=True, inplace=True)

print(historical)

# COMMAND ----------

# This command creates a view or table from the imported CSV file that can be manipulated using SQL rather than Python

temp_table_name = "AlgorandReport_csv"

df.createOrReplaceTempView(temp_table_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC /* Querying the created temp table in a SQL cell to show all the records now in the new MySQL temp_table */
# MAGIC 
# MAGIC select * from `AlgorandReport_csv` 

# COMMAND ----------

# MAGIC %sql
# MAGIC --First quarter values from ALgorand for 2022
# MAGIC --To review the coin's performance during the Q1 fiscal year, a separate view is created here from the temp-table data 
# MAGIC /* Query the created temp table in a SQL cell */
# MAGIC CREATE OR REPLACE TEMP VIEW q1_algorand_results 
# MAGIC AS select algorandReport_csv._c0 as DayMonthYear, algorandReport_csv._c1 as Price,algorandReport_csv._c5 as Volume  from `AlgorandReport_csv` where AlgorandReport_csv._c0 >= "1/1/2022" and AlgorandReport_csv._c0 <= "3/31/2022"

# COMMAND ----------

# MAGIC %sql
# MAGIC --average price and volume for Q1 
# MAGIC --This query from the view created above shows the average price the Algorand currency traded at during Q1. It also shows the average volume of the Algorand currency 
# MAGIC --select * from q1_algorand_results
# MAGIC select AVG(Price) as AveragePrice, AVG(Volume) as AverageVolume FROM q1_algorand_results

# COMMAND ----------

# MAGIC %sql
# MAGIC -- This query creates a separate view to view the mid Q2 data on the Algorand currency. The Q2 has not come to an end as of yet, so this view will contain all of the data from the beginning of second quarter to the current date of 6/9/2022
# MAGIC CREATE OR REPLACE TEMP VIEW q2_algorand_results 
# MAGIC AS select algorandReport_csv._c0 as DayMonthYear, algorandReport_csv._c1 as Price,algorandReport_csv._c5 as Volume  from `AlgorandReport_csv` where AlgorandReport_csv._c0 >= "4/1/2022" and AlgorandReport_csv._c0 <= "6/9/2022"

# COMMAND ----------

# MAGIC %sql
# MAGIC --This query from the view created above shows the average price the Algorand currency traded at during Q1. It also shows the average volume of the Algorand currency 
# MAGIC --select * from q2_algorand_results
# MAGIC select AVG(Price) as AveragePrice, AVG(Volume) as AverageVolume FROM q2_algorand_results

# COMMAND ----------

# With this registered as a temp view, it will only be available to this particular notebook. If you'd like other users to be able to query this table, you can also create a table from the DataFrame.
# Once saved, this table will persist across cluster restarts as well as allow various users across different notebooks to query this data.
# To do so, uncomment the bottom line.

permanent_table_name = "AlgorandReport_csv"

# df.write.format("parquet").saveAsTable(permanent_table_name)

# COMMAND ----------

# The dataframes created with the first few commands initialized data frames with the default headers. To provide better readability for the data retrieved from the CSV file, 
# the header names were changed so the column names reflect the data in the columns accurately 
# File location and type
file_location = "/FileStore/tables/AlgorandReport.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

newheaders = df.withColumnRenamed("_c0", "Date").withColumnRenamed("_c1", "Open").withColumnRenamed("_c2", "24hr_High").withColumnRenamed("_c3", "24hr_Low").withColumnRenamed("_c4", "Closing_price").withColumnRenamed("_c5", "Volume")

display(newheaders)
