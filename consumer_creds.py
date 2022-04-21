import os

import requests

from dotenv import load_dotenv
load_dotenv()


class APIConsumer():
    """Consumer credentials required to access Covario services"""
    def __init__(self):
        """
        :params: account_id: account ID to for covario identity.
        :params: fund_id: fund ID to for the associated covario quantity.
        :params: access_token: token retrieved from the authentication service.
        """
        self.account_id = os.getenv('ACCOUNT_ID')
        self.fund_id = os.getenv('FUND_ID')
        self.access_token = self.get_token()

        self.base_url = 'api-demo.covar.io/v2'

    def get_token(self):
        """
        Get token for account based on credentials in identity.

        :params: client_id: ID for the client associated.
        :params: client_secret: secret for the client associated.
        """

        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        IDENTITY_URL = os.getenv('ACCOUNT_TOKEN_URL')

        data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
        resp = requests.post(IDENTITY_URL, data=data)
        if resp.status_code != 200:
            raise Exception('No suitable token to take on the following steps! Contact support to get new client_credentials.')
        token = resp.json()['access_token']
        print('Token received successfully!')
        return token
