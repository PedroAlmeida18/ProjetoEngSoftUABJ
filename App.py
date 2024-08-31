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
from utils import cores, objetivos
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"Mensagem": "Bem-vindo ao jogo war, Você precisa escolher a cor do Exercito",
            "Cor do Exército" : "1-Azul, 2-Branca, 3-Vermelha, 4-Preta, 5-Amarela, 6-Verde",
            "Mensagem ": "Para seguir o jogo altere a rota para /escolher-cor/numero da sua cor"}


@app.get("/escolher-cor/{cor}")
async def escolher_cor(cor):
    return {
                "Mensagem": "Você escolheu a cor", 
                "Cor": cores[int(cor)],
                "Mensagem ": "Após a cor desejada selecionada mude a rota para ReceberObjetivo e receba o obejtivo no jogo"
            }

@app.get("/ReceberObjetivo/")
async def ReceberObjetivo():
    objetivo=random.choice(objetivos)
    return {
                "Mensagem": "Você recebeu o objetivo", 
                "Objetivo":  objetivo["Objetivos"]
            }

