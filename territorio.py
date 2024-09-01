import random


territorios = [
    {'id': 1, 'Região': 'América do Sul', 'Território': 'Brasil'},
    {'id': 2, 'Região': 'América do Sul', 'Território': 'Argentina/Uruguai'},
    {'id': 3, 'Região': 'América do Sul', 'Território': 'Colômbia/Venezuela'},
    {'id': 4, 'Região': 'América do Sul', 'Território': 'Peru/Bolívia/Chile'},
    {'id': 5, 'Região': 'América do Norte', 'Território': 'México'},
    {'id': 6, 'Região': 'América do Norte', 'Território': 'Califórnia'},
    {'id': 7, 'Região': 'América do Norte', 'Território': 'Nova Iorque'},
    {'id': 8, 'Região': 'América do Norte', 'Território': 'Labrador'},
    {'id': 9, 'Região': 'América do Norte', 'Território': 'Ottawa'},
    {'id': 10, 'Região': 'América do Norte', 'Território': 'Vancouver'},
    {'id': 11, 'Região': 'América do Norte', 'Território': 'Mackenzie'},
    {'id': 12, 'Região': 'América do Norte', 'Território': 'Alasca'},
    {'id': 13, 'Região': 'América do Norte', 'Território': 'Groenlândia'},
    {'id': 14, 'Região': 'Europa', 'Território': 'Islândia'},
    {'id': 15, 'Região': 'Europa', 'Território': 'Inglaterra'},
    {'id': 16, 'Região': 'Europa', 'Território': 'Suécia'},
    {'id': 17, 'Região': 'Europa', 'Território': 'Alemanha'},
    {'id': 18, 'Região': 'Europa', 'Território': 'Espanha/Portugal/França/Itália'},
    {'id': 19, 'Região': 'Europa', 'Território': 'Polônia/Iugoslávia'},
    {'id': 20, 'Região': 'Europa', 'Território': 'Moscou'},
    {'id': 21, 'Região': 'África', 'Território': 'Argélia/Nigéria'},
    {'id': 22, 'Região': 'África', 'Território': 'Egito'},
    {'id': 23, 'Região': 'África', 'Território': 'Congo'},
    {'id': 24, 'Região': 'África', 'Território': 'Sudão'},
    {'id': 25, 'Região': 'África', 'Território': 'Madagascar'},
    {'id': 26, 'Região': 'África', 'Território': 'África do Sul'},
    {'id': 27, 'Região': 'Ásia', 'Território': 'Oriente Médio'},
    {'id': 28, 'Região': 'Ásia', 'Território': 'Aral'},
    {'id': 29, 'Região': 'Ásia', 'Território': 'Omsk'},
    {'id': 30, 'Região': 'Ásia', 'Território': 'Dudinka'},
    {'id': 31, 'Região': 'Ásia', 'Território': 'Sibéria'},
    {'id': 32, 'Região': 'Ásia', 'Território': 'Tchita'},
    {'id': 33, 'Região': 'Ásia', 'Território': 'Mongólia'},
    {'id': 34, 'Região': 'Ásia', 'Território': 'Vladivostok'},
    {'id': 35, 'Região': 'Ásia', 'Território': 'China'},
    {'id': 36, 'Região': 'Ásia', 'Território': 'Índia'},
    {'id': 37, 'Região': 'Ásia', 'Território': 'Japão'},
    {'id': 38, 'Região': 'Ásia', 'Território': 'Vietnã'},
    {'id': 39, 'Região': 'Oceania', 'Território': 'Bornéu'},
    {'id': 40, 'Região': 'Oceania', 'Território': 'Sumatra'},
    {'id': 41, 'Região': 'Oceania', 'Território': 'Nova Guiné'},
    {'id': 42, 'Região': 'Oceania', 'Território': 'Austrália'}
]

def receber_carta_território():
    if not territorios:
        return {'Não há mais cartas de território'}
    territorio_recebido = random.choice(territorios)
    territorios.remove(territorio_recebido)
    return {
        "Titulo": f'Você recebeu o território',
        "Territorio": territorio_recebido['Território'],
    }