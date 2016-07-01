# Tapioca cartola

## Instalação
```
pip install tapioca-cartola

```

## Documentação

``` python

from tapioca_cartola import Cartola

# Acessando as api's publicas
cartola_api = Cartola()
cartola_api.mercado_destaques().get()

# Acessando as api's privadas, necessário o token
cartola_api.auth_time(access_token='token').get()

# Como diabos eu pego o token?!
from tapioca_cartola.auth import get_access_token

token = get_access_token(email='your@email.com', password='secret!')
cartola_api = Cartola(access_token=token)
cartola_api.auth_time().get()

```

## Testes e Cobertura de testes

Caso queira rodar os testes de login e senha, é necessário
definir duas variáveis de ambiente.: `CARTOLA_EMAIL` e `CARTOLA_PASSWORD`.

```
Name                           Stmts   Miss  Cover
--------------------------------------------------
tapioca_cartola/__init__.py        4      0   100%
tapioca_cartola/auth.py           12      0   100%
tapioca_cartola/cartola.py        13      0   100%
tapioca_cartola/override.py       31      0   100%
tapioca_cartola/resources.py       1      0   100%
--------------------------------------------------
TOTAL                             61      0   100%

========== 5 passed in 1.57 seconds ==============
```

## Roadmap

* Adicionar suporte para paginação
* Documentar endpoints com explicações e exemplos
* Adicionar compatibilidade com Python3

---

Caso tenha dúvidas de como utilizar a biblioteca, acesse a documentação do [Tapioca Wrapper](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
