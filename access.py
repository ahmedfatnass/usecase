import requests
import base64


class Access:

    def __init__(self):
        self.client_id = 'f7ac44a1-8cd1-46bb-896a-025fd6bc7731'
        self.client_secret = '9ab4625f-76e9-415e-9c09-01e58074b00b'
        self.content_type = 'application/x-www-form-urlencoded'
        self.to_encode = self.client_id + ':' + self.client_secret
        self.url_request = "https://digital.iservices.rte-france.com/token/oauth/"

    def get_token(self):
        base64_encoded_id_secret = base64.b64encode(self.to_encode.encode()).decode()
        headers = {
            'Content-Type': self.content_type,
            'Authorization': 'Basic {}'.format(base64_encoded_id_secret)
            }
        r = requests.post(self.url_request, headers=headers)

        token = r.json()['access_token']

        return token
