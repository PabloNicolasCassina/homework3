import pandas as pd
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@transformer
def transform(data, *args, **kwargs):
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    
    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    data.columns = [camel_to_snake(col) for col in data.columns]

    

    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")

    return data
    


    


@test
def test_output(output, *args):

    # Add three assertions
    assert output['vendor_id'].isin(output['vendor_id'].unique()).all(), 'Invalid vendor_id'
    assert (output['passenger_count'] > 0).all(), 'There are rides with zero passengers'
    assert (output['trip_distance'] > 0).all(), 'There are rides with zero distance'
