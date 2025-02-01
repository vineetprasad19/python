# Load Data into a Data Warehouse (BigQuery)
# This script uploads data from a CSV file to Google BigQuery.

from google.cloud import bigquery
import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('data.csv')

# BigQuery client
client = bigquery.Client()

# Define table and schema
table_id = 'my_project.my_dataset.my_table'
job = client.load_table_from_dataframe(df, table_id)

# Wait for the job to complete
job.result()
print("Data loaded into BigQuery.")