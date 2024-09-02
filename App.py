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

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from cor import cores, escolha_cor
from territorio import receber_carta_território
from objetivos import escolher_objetivo_aleatorio
from exercito import receber_exercito_inicial, colocar_exercito

import random

app = FastAPI()

territorios_recebido =[]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
                <head>
                </head>
                <body>
                    <h1> Bem Vindo ao jogo War</h1>
                    <p> Você precisa definir o número de Participantes para iniciar o jogo, podendo jogar até 6 pessoas.</p>
                    <form action="/escolhernumeroPartipantes" method="post">
                     <p> Digite abaixo o número de Participantes :  </p>
                    <input type = "number" name ="numero_Participantes" min ="2" max="6" requerid </input>
                    <button type = "submit">Enviar</button>
                    </form>
                </body>
        <html>
        """
@app.post("/escolhernumeroPartipantes", response_class=HTMLResponse)
async def escolher_numero_participantes(numero_Participantes: int = Form(...)):
    return f"""
        <html>
                <head>
                </head>
                    <h1>Jogo iniciado com {numero_Participantes} participantes!</h1>
                    <p> Agora os participantes irão escolher suas cores dos exercitos para continuar o jogo</p>
                    <p> 1- Azul, 2 - Branco, 3- Vermelha, 4 - Preta , 5 - Amarela, 6 - Verde </p>
                    <p>"Para seguir o jogo altere a rota para /escolher-cor/numero da sua cor" quantas vezes for preciso </p>
                <body>
            </html>
            """

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

