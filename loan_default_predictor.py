import joblib
import requests
from requests.auth import HTTPBasicAuth
import json


while 1:
    # 426484
user_id = input("Please enter the user id:")
# 67
branch_id = input("Please enter the branch id:")
# 12345
amount = float(input("Please enter the loan amount:"))

# Load the binary classifier.
logreg = joblib.load("loan_default_predictor.joblib")

URL = "https://app.tecton.ai/api/v1/feature-service/get-features"

DATA = {
    "params": {
        'feature_service_name': 'loan_default_feature_service',
        'join_key_map': {
            'UNIQUEID': user_id,
            'branch_id': branch_id
        },
        'request_context_map': {
            'DISBURSED_AMOUNT': amount
        },
        'workspace_name': 'jiadong-loan-live'
    }
}

data_to_send = json.dumps(DATA).encode("utf-8")
r = requests.post(url=URL, data=data_to_send, headers={
    "authorization": "Tecton-key 825ee1ed442fc808fa208faa89e029c5"})
print(r.json())
x = [r.json()['result']['features']]
print(x)
pred = logreg.predict(x)

if pred:
    print('The loan that user with id {} applies is very likely to default!!'.format(user_id))
else:
    print('The loan that user with id {} applies is not likely to default'.format(user_id))
