# -*- coding: utf-8 -*-


RESOURCE_MAPPING = {
    # status do mercado
    'mercado_status': {
        'resource': '/mercado/status',
    },
    # lista dos jogadores mais escalados
    'mercado_destaques': {
        'resource': '/mercado/destaques',
    },
    # lista de patrocinadores
    'patrocinadores': {
        'resource': '/patrocinadores',
    },
    # lista das rodadas do campeonato (1 até 38)
    'rodadas': {
        'resource': '/rodadas',
    },
    # próximas partidas do campeonato
    'partidas': {
        'resource': '/partidas',
    },
    # lista de clubes
    'clubes': {
        'resource': '/clubes',
    },
    # lista de todos os jogadores (retorna todas as informações)
    'atletas_mercado': {
        'resource': '/atletas/mercado',
    },
    # pontuação da rodada em andamento
    'atletas_pontuados': {
        'resource': '/atletas/pontuados',
    },
    # time que mais pontuou na rodada anterior
    'pos_rodada_destaques': {
        'resource': '/pos-rodada/destaques',
    },
    # busca geral de times, vai retornar info do time e o slug
    'times': {
        'resource': '/times?q={nome}',
    },
    # busca informações de um time específico, usar o slug do time.
    'time': {
        'resource': '/time/{slug}',
    },
    # busca geral de ligas, para consultar uma liga
    'ligas': {
        'resource': '/ligas?q={nome}',
    },
    # retornar todas as ligas do usuário logado.
    'auth_ligas': {
        'resource': '/auth/ligas',
        'protected': True,
    },
    # busca informações de uma liga específica, usar o slug da liga.
    'auth_liga': {
        'resource': '/auth/liga/{slug}',
        'protected': True,
    },
    # retornar informações do time do usuario logado.
    'auth_time': {
        'resource': '/auth/time',
        'protected': True,
    },
    'auth_time_info': {
        'resource': '/auth/time/info',
        'protected': True,
    }
}
