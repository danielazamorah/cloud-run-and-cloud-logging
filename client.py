import requests
import time
import logging
from google.cloud import logging_v2

import os

service_url = os.environ["CLOUD_RUN_SERVICE_URL"]
project_id = os.environ["PROJECT_ID"]


# Cloud Logging setup
logging_client = logging_v2.Client(project=project_id)
logger = logging_client.logger('cloud_run_async_calls')

def call_cloud_run(sku, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.post(
                service_url, 
                json={'sku': sku}
            )
            response.raise_for_status()

            # Log success
            logger.log_struct(
                {'sku': sku, 'status': 'success', 'attempt': retries + 1}
            )
            return response

        except requests.RequestException as e:
            retries += 1
            # Log failure
            logger.log_struct(
                {'sku': sku, 'status': 'failure', 'attempt': retries, 'error': str(e)}
            )

            # Retry after a delay (exponential backoff)
            time.sleep(2 ** retries)

    # All retries failed
    logger.log_struct({'sku': sku, 'status': 'failed_all_retries'})
    return None  # or raise a custom exception

if __name__ == '__main__':
    for sku_number in range(1, 11):  # Iterate from 1 to 10
        sku = f"SKU{sku_number}"  # Format the SKU (e.g., SKU1, SKU2, etc.)
        result = call_cloud_run(sku)
        print(f"Result for SKU {sku}: {result}")