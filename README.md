# Data Pipeline - FakeStore API

## Overview
This project is a minimal data pipeline built for a coding case study.  
It performs the following ETL concepts on data accessible from [FakeStore API](https://fakestoreapi.com/):
- **Fetch**: Get data from the [Products endpoint](https://fakestoreapi.com/products) of the API.
- **Store**: Save raw data as JSON.
- **Transform**: Produce a  metric — average product price per category.

---

## How to Run

### Prerequisites:
- Python 3.7+

### Steps
1. Clone this repo:
   ```bash
   git clone https://github.com/ShivaBP/fakestoreapi.git
   cd <root of the repository>

2. Create a virtual environment and install dependencies:

    -  Create a python virtual environment
    -  Run
        ```bash
        pip install -r requirements.txt

3. Run the pipeline:
    ```bash
    python pipeline.py

## Expected outputs: 
A folder named data containing:

- Raw data: data/raw/

- Transformed data: data/processed/


## Notes and assumptions:
- Only /products endpoint is used.
- The metric addressed in data transformation is average price per product.
- Local storage is used for simplicity. (Further discussion provided in a seperate document)