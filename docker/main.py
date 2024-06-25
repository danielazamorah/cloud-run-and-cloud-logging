import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Probability of failure (adjust as needed)
FAILURE_PROBABILITY = 0.3

@app.route('/', methods=['POST'])
def process_sku():
    data = request.get_json()
    sku = data.get('sku')
    if random.random() < FAILURE_PROBABILITY:
        return jsonify({"error": f"Failed to process SKU: {sku}"}), 500
    else:
        return jsonify({"message": f"Successfully processed SKU: {sku}"}), 200