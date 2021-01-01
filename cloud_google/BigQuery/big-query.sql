SELECT myjson
, mydatetime
, json_extract_scalar(myjson, '$.payload_fields.Latitude') as latitude
, json_extract_scalar(myjson, '$.payload_fields.Longitude') as longitude
FROM `clouds-1-cat.example_dataset.my_table_name` 
LIMIT 1000;

