#Objetivos  - Jogar War no navegador
#Url Base - LocalHost
#End Points - Preparação, distribuir exercitos, rodada
#localHost/preparação/cor(Get)
#localHost/preparação/objetivo(Get)
#localHost/preparação/corEnv(Post)

#localHost/Distribuir/OrdemJogadores(Get)
#localHost/Distribuir/Territórios(Get)
#localHost/Distribuir/Exercitos(Get)
#localHost/Distribuir/Exercitos/Distribuir(Post)
#Quais recursos : Jogo War

from fastapi import FastAPI
from utils import cores, objetivos, territorios
import random

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Titulo": "Bem-vindo ao jogo war, Você precisa escolher a cor do Exercito",
        "Cor do Exército" : "1-Azul, 2-Branca, 3-Vermelha, 4-Preta, 5-Amarela, 6-Verde",
        "Mensagem ": "Para seguir o jogo altere a rota para /escolher-cor/numero da sua cor"
    }


@app.get("/escolher-cor/{cor}")
async def escolher_cor(cor):
    return {
        "Titulo": "Você escolheu a cor", 
        "Cor": cores[int(cor)-1],
        "Mensagem ": "Após a cor desejada selecionada mude a rota para ReceberObjetivo e receba o obejtivo no jogo"
    }


@app.get("/ReceberObjetivo/")
async def ReceberObjetivo():
    objetivo=random.choice(objetivos)
    return {
        "Titulo": "Você recebeu o objetivo", 
        "Objetivo":  objetivo["Objetivos"],
        "Mensagem": "Para saber qual sua vez de jogar acesse a rota ordem-jogadores",
    }


@app.get("/ordem-jogadores/")
async def definir_ordem():
    ordem = random.randint(1, 6)
    return {
        "Titulo": f"Você será o {ordem}° jogador a jogar",
        "Ordem": ordem,
        "Mensagem": "Para saber seu território inicial acesse a rota meus-territorios",
    }


@app.get("/meus-territorios")
async def meus_territorios():
    territorio = random.choice(territorios)
    return {
        "Titulo": f'Você recebeu o território',
        "Territorio": territorio['Território'],
    }
