# homework3

SQL Queries used to resolve the task

I used the "Homework3" pipeline to upload the data to gcs

CREATE OR REPLACE EXTERNAL TABLE ny_taxi.external_green_taxi_trip_records_2022
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-nico-ca-30/nyc_green_taxi_2022.parquet']
);


CREATE OR REPLACE TABLE datatalks-course.ny_taxi.native_green_taxi_trip_records_2022
AS
SELECT * FROM ny_taxi.external_green_taxi_trip_records_2022;

-- Q1

SELECT COUNT (*) FROM ny_taxi.native_green_taxi_trip_records_2022;

-- Q2

SELECT COUNT (DISTINCT(PULocationID))
FROM ny_taxi.native_green_taxi_trip_records_2022;

SELECT COUNT (DISTINCT(PULocationID))
FROM ny_taxi.external_green_taxi_trip_records_2022;

-- Q3

SELECT COUNT (*)
FROM ny_taxi.external_green_taxi_trip_records_2022
WHERE fare_amount = 0;

-- Q4

CREATE OR REPLACE TABLE ny_taxi.green_tripdata_partitioned_clustered
PARTITION BY pickup_date
CLUSTER BY PUlocationID AS
SELECT *
FROM ny_taxi.external_green_taxi_trip_records_2022;

--Q5

-- 9.82MB

SELECT *
FROM ny_taxi.green_tripdata_partitioned_clustered
WHERE pickup_date BETWEEN '2022-06-01' AND '2022-06-30';

-- 114MB

SELECT *
FROM ny_taxi.native_green_taxi_trip_records_2022
WHERE pickup_date BETWEEN '2022-06-01' AND '2022-06-30';