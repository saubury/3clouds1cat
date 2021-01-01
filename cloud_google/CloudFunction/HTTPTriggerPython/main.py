import json
from datetime import datetime
from google.cloud import bigquery

def http_request(request):

    print('http_request started')
    request_json = request.get_json()

    if request_json:
        # request_json is a dictionary; convert dictionary into string using json.dumps() 
        result_json_string = json.dumps(request_json) 

        # Construct a BigQuery client object.
        client = bigquery.Client()

        # Prepares a reference to the dataset
        dataset_ref = client.dataset('example_dataset')
        table_ref = dataset_ref.table('my_table_name')
        table = client.get_table(table_ref)  # API call
        rows_to_insert = [
            (u'TEST', 1, result_json_string, datetime.now()),
        ]
        errors = client.insert_rows(table, rows_to_insert)  # API request
        assert errors == []

    return f'Done!'
