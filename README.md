# Cloud Run and Cloud logging
In this repository, we'll test the integration of Cloud Run and Cloud Logging to create a "retry &amp; alert" logic.

First, we craft a dummy Cloud Run service to test your logging, retry, and alerting logic. To test the dummy service locally, run the following commands:

```bash
cd docker
```
```bash
docker build -t dummy-service .
```
```bash
docker run -d -p 8080:8080 --name dummy-container dummy-service
```
```bash
python3 test.py
```

Run the last line a few times, you will get the responses `{'message': 'Successfully processed SKU: 1234'}` and `{'error': 'Failed to process SKU: 1234'}` with a 70-30 probability (you can modify this in [`main.py`](docker/main.py)).
