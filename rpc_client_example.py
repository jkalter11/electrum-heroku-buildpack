import requests
import json
import os
import util


def request(method, args=None):
    if args is None: args = []
    args.insert(0, os.environ["WALLET_NAME"])
    url = "http://localhost:9001/jsonrpc"
    headers = {'content-type': 'application/json'}
    payload = {
        "method": method,
        "params": args,
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    return response


def main():
    # some successful requests
    address = request("create_address")["result"]
    request("pay", [address, 0.0002, 0.0001])
    request("get_address_balance", [address])
    request("get_balance")

    # invalid fee (caught by script; fee > btc)
    request("pay", [address, 0.0002, 0.0003])
    # invalid fee (error in electrum; ridiculously high fee)
    request("pay", [address, 2, 1])


if __name__ == "__main__":
    main()
