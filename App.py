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

app = FastAPI()


@app.get("/")
async def root():
    return {"Mensagem": "Bem-vindo ao jogo war"}


@app.get("/escolher-cor/{cor}")
async def escolher_cor(cor):
    return {
                "Mensagem": "Você escolheu a cor", 
                "Cor": cores[int(cor)],
            }
