import json
from datetime import datetime
from google.cloud import bigquery

def http_request(request):

    print('http_request started')
    request_json = request.get_json()

    if request_json:
        # request_json is a dictionary; convert dictionary into string using json.dumps() 
        result_json_string = json.dumps(request_json) 
        print (f'Body: {result_json_string}')

        # Construct a BigQuery client object and prepares a reference to the dataset
        client = bigquery.Client()
        dataset_ref = client.dataset('cat_location_dataset')
        table_ref = dataset_ref.table('cat_location')
        table = client.get_table(table_ref)  # API call
        rows_to_insert = [  (datetime.now(), result_json_string),  ]
        errors = client.insert_rows(table, rows_to_insert)  # API request
        assert errors == []

    return (f'Done')
    
