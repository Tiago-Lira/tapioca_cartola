# -*- coding: utf-8 -*-

import tapioca
from .resources import RESOURCE_MAPPING
from .override import generate_wrapper_from_adapter


class CartolaAdapter(tapioca.JSONAdapterMixin, tapioca.TapiocaAdapter):

    api_root = 'https://api.cartolafc.globo.com'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(
            self, api_params={}, *args, **kwargs):
        params = super(CartolaAdapter, self).\
            get_request_kwargs(*args, **kwargs)

        access_token = api_params.get('access_token')
        if access_token:
            params['headers'].update({'X-GLB-Token': access_token})

        return params


Cartola = generate_wrapper_from_adapter(CartolaAdapter)
