from google.oauth2 import service_account
from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/james/BIGQUERY/MAIN/try_access_policy_bq/keys/key.json'

# Set the project ID and dataset ID
project_id = 'test-3-project-380217'
dataset_id = "test"
table_id = "test_people"
# client = bigquery.Client(project=project_id,credentials=credentials)
client = bigquery.Client()
# Get a reference to the table you want to set access controls for
table_ref = client.dataset('test').table('test_people')

table = client.get_table(table_ref)
# Set access controls for the table
policy = bigquery.IAMPolicy()
policy.viewers.add('user:viewer@example.com')
# policy.owners.add('user:owner@example.com')
table.iam_policy = policy
client.update_table(table, ['iam_policy'])