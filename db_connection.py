from dotenv import load_dotenv
import os
import mysql.connector

# Load environment variables from .env file
load_dotenv(dotenv_path="creds.env")

# Get values from .env
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("DB_NAME")

# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

print("Connected to MySQL!")