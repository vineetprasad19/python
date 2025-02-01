
# Extract Data from a CSV File and Load into a Database
# This script reads data from a CSV file and inserts it into a PostgreSQL database.

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load CSV into a DataFrame
df = pd.read_csv('data.csv')

# Database connection
engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')

# Load DataFrame into a database table
df.to_sql('my_table', engine, if_exists='replace', index=False)
print("Data loaded into the database.")