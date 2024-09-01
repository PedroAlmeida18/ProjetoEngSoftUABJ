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
from cor import cores, escolha_cor
from territorio import receber_carta_território
from objetivos import escolher_objetivo_aleatorio
from exercito import receber_exercito_inicial, colocar_exercito
import random

app = FastAPI()

territorios_recebido =[]

@app.get("/")
async def root():
    return {"Mensagem": "Bem-vindo ao jogo war, Você precisa escolher a cor do Exercito",
            "Cor do Exército" : "1-Azul, 2-Branca, 3-Vermelha, 4-Preta, 5-Amarela, 6-Verde",
            "Mensagem ": "Para seguir o jogo altere a rota para /escolher-cor/numero da sua cor"}


@app.get("/escolher-cor/{cor}")
async def escolher_cor(cor: int):
    return escolha_cor(cor)

    
@app.get("/receber-objetivo/")
async def Receber_objetivo():
    return escolher_objetivo_aleatorio()


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
    return receber_carta_território()

@app.get("/recebe-exercitos")
async def recebe_exercitos():
    return receber_exercito_inicial()

@app.get("/meus-territorios/{território}/{valor}")
async def por_exercito(territorios: str, valor: int):
    return colocar_exercito(territorios, valor)