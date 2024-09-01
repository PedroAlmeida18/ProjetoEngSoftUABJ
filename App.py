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
from objetivos import escolher_objetivo_aleatorio

app = FastAPI()


@app.get("/")
async def root():
    return {"Mensagem": "Bem-vindo ao jogo war, Você precisa escolher a cor do Exercito",
            "Cor do Exército" : "1-Azul, 2-Branca, 3-Vermelha, 4-Preta, 5-Amarela, 6-Verde",
            "Mensagem ": "Para seguir o jogo altere a rota para /escolher-cor/numero da sua cor"}


@app.get("/escolher-cor/{cor}")
async def escolher_cor(cor: int):
    return escolha_cor(cor)

    

@app.get("/ReceberObjetivo/")
async def ReceberObjetivo():
    return escolher_objetivo_aleatorio()

