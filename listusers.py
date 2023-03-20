from google.oauth2 import service_account
from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='...keys/key.json'

# Set the project ID and dataset ID
project_id = 'learned-answer-379305'
dataset_id = "test_1"
table_id = "test_1_people"
client = bigquery.Client()
# Get a reference to the table you want to set access controls for
table_ref = client.dataset(dataset_id).table(table_id)

table = client.get_table(table_ref)
# Set access controls for the table
policy = bigquery.IAMPolicy()
policy.viewers.add('user:viewer@example.com')
# policy.owners.add('user:owner@example.com')
table.iam_policy = policy
client.update_table(table, ['iam_policy'])
