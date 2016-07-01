# -*- coding: utf-8 -*-

import requests
from tapioca import exceptions


__all__ = ['get_access_token']


def get_access_token(email, password, service_id=438):
    url = u'https://login.globo.com/api/authentication'
    payload = {
        'payload': {
            'email': email,
            'password': password,
            'serviceId': service_id,
        }
    }
    response = requests.post(url, json=payload)
    data = response.json()
    if 'glbId' not in data:
        message = data.get('userMessage', None) or data.get('id')
        raise exceptions.ServerError(message)

    return data['glbId']
