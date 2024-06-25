import requests

# Replace with the SKU you want to test
sku = "1234"

port = 8080
try:
    response = requests.post(f'http://localhost:{port}/', json={'sku': sku})
    response.raise_for_status()  # Raise an exception for bad responses
    print(response.json())
except requests.RequestException as e:
    print(f"Request failed: {e}")
