from consumer_creds import APIConsumer

import os
import sys
import time
import json
import logging
from signalrcore.hub_connection_builder import HubConnectionBuilder

def generate_user_payload(
    consumer, base_currency='BTC', quote_currency='USD', quantity_currency='BTC', client_reference='Python test client'):
    """
    Generate the payload which needs to be sent to the API to start quote streaming.

    :params: consumer: API consumer object which is generated. See more in `consumer_creds.py`
    :params: base_currency: the base currency you want to change from.
    :params: quote_currency: the quote currency you want to change to.
    :params: client_reference: Client reference which helps us identify the client.
    """
    ## For the Python wrapper, only need to send `item1`.
    return {
        'accountId': consumer.account_id,
        'fundId': consumer.fund_id,
        'baseCurrency': base_currency,
        'quoteCurrency': quote_currency,
        'quantity': 1,
        'quantityCurrency': quantity_currency,
        'clientReference': client_reference
    }



if __name__ == '__main__':
    consumer = APIConsumer()

    ## Enable logging
    ## change logging.INFO to logging.DEBUG for testing/debugging
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    ## Start a hub connection to the OTC hub using SignalR
    otc_url = f'https://{consumer.base_url}/api/signalr/otcHub'
    hub_connection = HubConnectionBuilder().with_url(otc_url).with_automatic_reconnect({
            "type": "interval",
            "keep_alive_interval": 10,
            "intervals": [1, 3, 5, 7, 9, 10]
        }).configure_logging(logging.DEBUG, socket_trace=True, handler=handler).build()
    hub_connection.start()

    user_payload = generate_user_payload(consumer)
    hub_connection.on_open(lambda: print('Connection opened and handshake received'))

    try:
        ## Start quote stream and define event handlers
        hub_connection.stream(
            "StartQuote",
            [user_payload, consumer.get_token()]).subscribe({
                "next": lambda x: print(x),
                "complete": lambda x: print('Method is completed.'),
                "error": lambda x: print(f'Error reported: {x}')
        })

        ## Keep the process alive
        while True:
            continue
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    hub_connection.stop()
