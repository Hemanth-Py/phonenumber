import json
import uuid
import base64
from urllib import request, error

merchant_id = 'TEST222208056001'
username = f'merchant.{merchant_id}'
password = '925365443baa766101126b30a7792c73'

# Encode credentials
credentials = f'{username}:{password}'
encoded_credentials = base64.b64encode(credentials.encode()).decode()

print("Auth Header:", encoded_credentials)


def create_order():
    url = f'https://epayment.areeba.com/api/rest/version/82/merchant/{merchant_id}/session'
    new_order_id = str(uuid.uuid4())

    payload = {
        "apiOperation": "INITIATE_CHECKOUT",
        "interaction": {
            "operation": "AUTHORIZE",
            "merchant": {
                "name": "Test Merchant"
            },
            "displayControl": {
                "billingAddress": "HIDE"
            }
        },
        "order": {
            "currency": "USD",
            "id": new_order_id,
            "amount": 5,
            "description": "event Name",
            "custom": {
                "eventId": "EVENT123",
                "ticketId": "TICKET456",
                "khOrderId": "KONFHUB789012345678901234567890123456789"
            }
        }
    }

    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/json'
    }

    req = request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')

    try:
        with request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print("Status Code:", response.status)
            print("Response:", response_data)
            print("Order ID:", new_order_id)
    except error.HTTPError as e:
        print("HTTPError:", e.code, e.reason)
        print("Response body:", e.read().decode())
    except error.URLError as e:
        print("URLError:", e.reason)


# Call the function
create_order()
