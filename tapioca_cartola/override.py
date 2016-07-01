# -*- coding: utf-8 -*-

from tapioca import exceptions
from tapioca import tapioca


class ProtectedMixin(object):
    u"""TapiocaClient com a opção de resource "protected"

    Para adicionar quais recursos necessitam de login ou não, foi
    necessário implementar este mixin. Na API do cartola existem
    resources publicos e privados (login e senha).

    Com este mixin, é possível adicionar no resource uma nova key
    chamada "protected", que caso seja verdadeira, será necessário
    ter o "access_token" dentro de _api_params ou na chamada do resource.

    Eg.:
        api = ProtectedTapioca()
        api.protected_resource()
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            Traceback (most recent call last)
                ClientError: This resource is protected.
                You must inform "access_token" to use it.

        api.protected_resource(access_token="token")
        > OK

    """

    def __call__(self, *args, **kwargs):
        self._access_token = kwargs.get('access_token') or\
            self._api_params.get('access_token')
        return super(ProtectedMixin, self).__call__(*args, **kwargs)

    def _wrap_in_tapioca_executor(self, data, *args, **kwargs):
        request_kwargs = kwargs.pop('request_kwargs', self._request_kwargs)
        api_params = self._api_params.copy()
        resource = kwargs.get('resource')

        if self._resource_is_protected(resource):
            if not self._access_token:
                raise exceptions.ClientError(
                    u'This resource is protected. '
                    u'You must inform "access_token" to use it.')

            api_params['access_token'] = self._access_token

        return ProtectedTapiocaClientExecutor(
            self._instatiate_api(), data=data,
            api_params=api_params,
            request_kwargs=request_kwargs, *args, **kwargs)

    def _wrap_in_tapioca(self, data, *args, **kwargs):
        request_kwargs = kwargs.pop('request_kwargs', self._request_kwargs)
        return ProtectedTapiocaClient(
            self._instatiate_api(), data=data,
            api_params=self._api_params,
            request_kwargs=request_kwargs,
            *args, **kwargs)

    def _resource_is_protected(self, resource):
        if not resource:
            return False
        return resource.get('protected', False)


class ProtectedTapiocaClient(ProtectedMixin, tapioca.TapiocaClient):
    pass


class ProtectedTapiocaClientExecutor(
        ProtectedMixin, tapioca.TapiocaClientExecutor):
    pass


def generate_wrapper_from_adapter(adapter):

    def instantiator(serializer_class=None, **kwargs):
        adapter_instance = adapter(serializer_class=serializer_class)
        return ProtectedTapiocaClient(adapter_instance, api_params=kwargs)

    return instantiator
