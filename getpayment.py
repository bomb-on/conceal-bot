import requests
import json

def main():

    # simple wallet is running on the localhost and port of 18082
    url = "http://localhost:6061/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # an example of a payment id
    payment_id = "6ab8e5a232cc378f7b8877287184986d29a008537f58b241deb90ffb8bafbdb0"

    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "get_payments",
        "params": {"payment_id": payment_id}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    data = response.json()
    result = data["result"]
    payments = result["payments"]
    print(payments)    

if __name__ == "__main__":
    main()