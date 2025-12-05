# pip install pandas google-cloud-bigquery
# Ensure you have a service account JSON key file downloaded from Google Cloud IAM.

from google.cloud import bigquery
import pandas as pd

# Path to your service account key file
SERVICE_ACCOUNT_KEY = "path/to/service_account.json"

# Build a BigQuery client
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_KEY)

# Example SQL query
QUERY = """
SELECT *
FROM `project_id.dataset.table`
LIMIT 1000
"""

# Run the query and load results into a pandas DataFrame
df = client.query(QUERY).result().to_dataframe()

# Show output
print(df.head())
print(f"\nRows loaded: {len(df)}")


