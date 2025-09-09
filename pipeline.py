from datetime import datetime

import json
import os
import pandas as pd
import requests

BASE_URL = "https://fakestoreapi.com"

def fetch_data():
    '''
    Fetch data from https://fakestoreapi.com API products endpoint.
    Returned output is in json format.
    '''
    products_url = f"{BASE_URL}/products"
    response = requests.get(products_url)
    data = response.json()
    return data 


def store_raw(data):
    '''
    Raw data is stored locally in:
    - Path: data/raw/
    - Format: Original format - Json
    - Filename template: products_<yyyymmdd_HHMMSS>.json
    '''
    os.makedirs("data/raw", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"data/raw/products_{ts}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


def transform(data):
    """
    Transform raw product data to calculate average price per category-

    Steps:
      1. Convert JSON data into a pandas DataFrame for easier processing.
      2. Group data by category and price and calculate the average value.
      3. Save the result locally in:
        - Path: data/processed/
        - Format: parquet 
        - Filename template: avg_price_per_category_<yyyymmdd_HHMMSS>.parquet
    Returns the path to the transformed file.
    """
    df = pd.DataFrame(data)
    result = df.groupby("category")["price"].mean()

    os.makedirs("data/processed", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"data/processed/avg_price_per_category_{ts}.parquet"

    result.to_frame("avg_price").reset_index().to_parquet(path, index=False)
    return path

if __name__ == "__main__":
    print("Fetching data")

    data = fetch_data()

    raw_path = store_raw(data)
    print(f"Raw data stored at {raw_path}")

    transformed_path = transform(data)
    print(f"Transformed data stored at {transformed_path}")
    
    print("Pipeline complete!")
