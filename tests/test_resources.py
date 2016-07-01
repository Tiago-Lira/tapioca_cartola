# -*- coding: utf-8 -*-

import os
import pytest

from tapioca import exceptions
from tapioca_cartola.cartola import Cartola
from tapioca_cartola.auth import get_access_token


DISABLE_LOGIN = os.environ.get('DISABLE_LOGIN', False) == 'True'
CARTOLA_EMAIL = os.environ.get('CARTOLA_EMAIL', None)
CARTOLA_PASSWORD = os.environ.get('CARTOLA_PASSWORD', None)

CAN_TEST_LOGIN = (not CARTOLA_EMAIL or not CARTOLA_PASSWORD) or DISABLE_LOGIN


@pytest.fixture
def public_client():
    return Cartola()


@pytest.fixture
def protected_client():
    token = get_access_token(email=CARTOLA_EMAIL, password=CARTOLA_PASSWORD)
    return Cartola(access_token=token)


def test_api_publica(public_client):
    assert public_client.ligas().get() is not None


def test_api_protegida_deve_exigir_token(public_client):

    with pytest.raises(exceptions.ClientError):
        public_client.auth_ligas()

    with pytest.raises(exceptions.ClientError) as e:
        public_client.auth_ligas().get()

    assert e.value.message == (
        'This resource is protected. '
        'You must inform "access_token" to use it.'
    )


def test_access_token_invalido(public_client):
    with pytest.raises(exceptions.TapiocaException) as e:
        public_client.auth_ligas(access_token='fake').get()

    assert e.value.status_code == 401
    assert e.value.client.mensagem().data == u'Usuário não autorizado'


@pytest.mark.skipif(
    CAN_TEST_LOGIN,
    reason='requires credentials into environment variables')
def test_access_token_valido(protected_client):
    assert protected_client.auth_ligas().get() is not None


@pytest.mark.skipif(
    CAN_TEST_LOGIN,
    reason='requires credentials into environment variables')
def test_get_access_token_com_login_invalido():
    with pytest.raises(exceptions.TapiocaException) as e:
        get_access_token(email='fake', password='fake')

    assert e.value.message == u'Seu e-mail ou senha estão incorretos.'
