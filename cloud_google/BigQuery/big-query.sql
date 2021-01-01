SELECT DATETIME(mydatetime, "Australia/Sydney") as mydatetime_local
, json_extract_scalar(myjson, '$.payload_fields.Latitude') as latitude
, json_extract_scalar(myjson, '$.payload_fields.Longitude') as longitude
, ST_GeogPoint(cast(json_extract_scalar(myjson, '$.payload_fields.Longitude') as FLOAT64), cast(json_extract_scalar(myjson, '$.payload_fields.Latitude') as FLOAT64)) AS g
FROM `cat_location_dataset.cat_location` 
where mydatetime > TIMESTAMP "2021-01-01 14:15:00+11"
order by mydatetime