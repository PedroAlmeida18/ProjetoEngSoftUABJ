import random

objetivos = [
    {'id': 1, 'Objetivos': 'Conquistar na totalidade a EUROPA, a OCEANIA e mais um terceiro.'},
    {'id': 2, 'Objetivos': 'Conquistar na totalidade a ÁSIA e a AMÉRICA DO SUL.'},
    {'id': 3, 'Objetivos': 'Conquistar na totalidade a EUROPA, a AMÉRICA DO SUL e mais um terceiro.'},
    {'id': 4, 'Objetivos': 'Conquistar 18 TERRITÓRIOS e ocupar cada um deles com pelo menos dois exércitos.'},
    {'id': 5, 'Objetivos': 'Conquistar na totalidade a ÁSIA e a ÁFRICA.'},
    {'id': 6, 'Objetivos': 'Conquistar na totalidade a AMÉRICA DO NORTE e a ÁFRICA.'},
    {'id': 7, 'Objetivos': 'Conquistar 24 TERRITÓRIOS à sua escolha.'},
    {'id': 8, 'Objetivos': 'Conquistar na totalidade a AMÉRICA DO NORTE e a OCEANIA.'},
    {'id': 9, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS AZUIS.'},
    {'id': 10, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS AMARELOS.'},
    {'id': 11, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS VERMELHOS.'},
    {'id': 12, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS PRETOS.'},
    {'id': 13, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS BRANCOS.'},
    {'id': 14, 'Objetivos': 'Destruir totalmente OS EXÉRCITOS VERDES.'},
]

def escolher_objetivo_aleatorio():
    if not objetivos:
        return {"Nenhum objetivo disponível para escolher."}
    
    objetivo_escolhido = random.choice(objetivos)
    objetivos.remove(objetivo_escolhido)
    return {
        "Mensagem": "Você escolheu o objetivo",
        "Objetivo": objetivo_escolhido['Objetivos'],
        "Mensagem2": "O objetivo foi removido da lista de objetivos disponíveis."
    }
