import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_green_taxi(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-"
    
    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID': pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra': float,
                    'mta_tax': float,
                    'tip_amount': float,
                    'tolls_amount': float,
                    'improvement_surcharge': float,
                    'total_amount': float,
                    'congestion_surcharge': float
                }

    months = [10, 11, 12]

    green_taxi_etl = pd.DataFrame()

    for month in months:
    # Genera la URL completa para el mes actual
        current_url = f"{url}{str(month).zfill(2)}.csv.gz"
        
        # Carga los datos del mes actual en un dataframe temporal
        current_data = pd.read_csv(current_url, parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'])
        
        # Concatena el dataframe temporal al dataframe principal
        if green_taxi_etl.empty:
            green_taxi_etl = current_data.copy()
        else:
            green_taxi_etl = pd.concat([green_taxi_etl, current_data], ignore_index=True)

# Muestra las primeras filas del dataframe resultante
    

    parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']


    return green_taxi_etl




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'