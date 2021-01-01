

# Deploying Cloud Function

```
gcloud functions deploy HTTPTriggerPython --runtime python38 --trigger-http --allow-unauthenticated --entry-point http_request --region australia-southeast1
```


# Setup Big Query
Create table
```sql
 CREATE TABLE cat_location_dataset.cat_location
 (
   mydatetime TIMESTAMP,
   myjson STRING
 )
 ```

# Testing Cloud Function

```bash
curl --header "Content-Type: application/json"   --request POST   --data '{"message":"Test HTTP Call", "city":"Sydney"}' https://australia-southeast1-clouds-1-cat.cloudfunctions.net/HTTPTriggerPython

```

# BigQuery

```sql
SELECT DATETIME(mydatetime, "Australia/Sydney") as mydatetime_local
, json_extract_scalar(myjson, '$.payload_fields.Latitude') as latitude
, json_extract_scalar(myjson, '$.payload_fields.Longitude') as longitude
, ST_GeogPoint(cast(json_extract_scalar(myjson, '$.payload_fields.Longitude') as FLOAT64), cast(json_extract_scalar(myjson, '$.payload_fields.Latitude') as FLOAT64)) AS g
FROM `cat_location_dataset.cat_location` 
where mydatetime > TIMESTAMP "2021-01-01 14:15:00+11"
order by mydatetime
```