import requests
import json
import os
from flask import Flask, send_file

measurement_id = os.environ.get('MEASUREMENT_ID')
api_secret = os.environ.get('API_SECRET')

app = Flask(__name__)


@app.route('/zer0pts.png')
def zer0pts_png():
    r = requests.post(f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}", json={
        "client_id": 'crypto-writeup-public-ga4-measurement-protocol-proxy',
        "events": [{
            "name": 'access',
            "params": {},
        }],
    })

    print(r.status_code)


    return send_file('./zer0pts.png')


if __name__ == '__main__':
    app.run()




