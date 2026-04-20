# pip install mlflow
# pip install azureml-mlflow

# pip install azure-ai-ml
# pip install azure-identity

# 모델 생성 시 conda.yaml에서도...
# - pip
#   - azureml-ai-monitoring
#   - azureml-inference-server-http
#   - inference-schema

import os
import urllib.request
import json

data = {
    "input_data": {"columns": ["fight", "yok"], "index": [0], "data": [[80, 20]]},
}

body = str.encode(json.dumps(data))

url = os.environ["AZURE_ML_ENDPOINT"]
api_key = os.environ["AZURE_ML_KEY"]
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": ("Bearer " + api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)[0]
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
