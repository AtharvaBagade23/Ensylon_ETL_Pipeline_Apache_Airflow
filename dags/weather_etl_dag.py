from airflow.sdk import dag, task
from datetime import datetime
import requests
import pandas as pd
import sqlite3
from io import StringIO

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=18.52&longitude=73.85&hourly=temperature_2m,relative_humidity_2m"


@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["etl", "weather"]
)
def weather_etl_pipeline():

    # -------------------------
    # Extract
    # -------------------------
    @task
    def extract_weather():

        response = requests.get(API_URL)
        response.raise_for_status()   # good practice

        return response.json()

    # -------------------------
    # Transform
    # -------------------------
    @task
    def transform_weather(data):

        df = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temperature": data["hourly"]["temperature_2m"],
            "humidity": data["hourly"]["relative_humidity_2m"]
        })

        # convert timestamp to string (important for XCom)
        df["time"] = pd.to_datetime(df["time"]).astype(str)

        df = df.head(24)

        return df.to_json()

    # -------------------------
    # Load
    # -------------------------
    @task
    def load_weather(records):

        df = pd.read_json(StringIO(records))

        print("Dataframe received in load step:")
        print(df.head())
        print("Rows:", len(df))

        conn = sqlite3.connect("/usr/local/airflow/weather.db")

        df.to_sql(
            "weather_data",
            conn,
            if_exists="append",
            index=False
        )

        conn.commit()
        conn.close()

    data = extract_weather()
    cleaned = transform_weather(data)
    load_weather(cleaned)


weather_etl_pipeline()