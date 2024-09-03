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

from fastapi import FastAPI, Query, Form
from fastapi.responses import HTMLResponse
from cor import cores, escolha_cor
from territorio import receber_carta_território
from objetivos import escolher_objetivo_aleatorio
from exercito import receber_exercito_inicial, colocar_exercito

import random

app = FastAPI()
numero_Participantes=None
territorios_recebido = []

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head></head>
            <body>
                <h1>Bem-Vindo ao jogo War</h1>
                <p>Você precisa definir o número de Participantes para iniciar o jogo, podendo jogar até 6 pessoas.</p>
                <form action="/escolhernumeroPartipantes" method="post">
                    <p>Digite abaixo o número de Participantes:</p>
                    <input type="number"id="numero_Participantes" name="numero_Participantes" min="2" max="6" required>
                    <button type="submit">Enviar</button>
                </form>
            </body>
        </html>
    """

@app.post("/escolhernumeroPartipantes", response_class=HTMLResponse)
async def escolher_numero_participantes(numero_Participantes: int = Form(...)):
    definir_ordem(numero_Participantes)
    return f"""
        <html>
            <head></head>
            <body>
                <h1>Jogo iniciado com {numero_Participantes} participantes!</h1>
                <h2>{definir_ordem(numero_Participantes)}</h2>
                <p>Agora os participantes irão escolher suas cores dos exércitos para continuar o jogo.</p>
                <p>1- Azul, 2 - Branco, 3- Vermelha, 4 - Preta, 5 - Amarela, 6 - Verde</p>
                <form action="/escolher-cor/" method="get">
                    <label for="numero_cor">Escolha sua cor (1-6):</label>
                    <input type="number" id="numero_cor" name="numero_cor" min="1" max="6" required>
                    <button type="submit">Confirmar cor</button>
                </form>
                <form action = "/" method="get"/>
                    <button type="submit">Voltar página </button>
                </form>
            </body>
        </html>
    """

@app.get("/escolher-cor/", response_class=HTMLResponse)
async def escolher_cor(numero_cor: int = Query(...)):
    resultado = escolha_cor(numero_cor)
    return f"""
        <html>
            <head></head>
            <body>
                <h1>{resultado['Mensagem']}</h1>
                <p>Cor escolhida: {resultado['Cor']}</p>
                <p>{resultado['Mensagem2']}</p>
                <p> Descubra 1° os seus territórios e após isso vá descobrir seus objetivos. O último a descobrir o objetivo deve preencher o campo para saber a ordem das rodadas</p>
                 <form action = "/meus-territorios"" method ="get">
                <label for="numero_cor">Digite seu id para descobrir seus territórios:</label>
                <input type="number" id="numero_cor" name="numero_cor" min="1" max="6" required>
                    <button type="submit">Receber Territórios</button>
                </form>
                
                <form action = "/receber-objetivo/" method ="get">
                <label for="numero_cor">Digite seu id  com base no número da cor (1-6):</label>
                <input type="number" id="numero_cor" name="numero_cor" min="1" max="6" required>
                    <button type="submit">Receber objetivo</button>
                </form>
                
                <button onclick="history.back()">Voltar</button>     
            </body>
        </html>
    """

@app.get("/receber-objetivo/", response_class=HTMLResponse)
async def receber_objetivo(numero_cor: int = Query(...)):
     objetivo=escolher_objetivo_aleatorio()
     return f"""
         <html>
            <head></head>
            <body>
                <h1>{objetivo['Objetivo']}</h1>
                <p>Para saber a ordem do jogadores digite novamente o número de Participantes<p>
                 <form action ="/ordem-jogadores/" method="get">
                 <input type="number"id="numero_Participantes" name="numero_Participantes" min="2" max="6" required>
                 <button type="submit">Ordem das jogadas</button>
                 </form>
           <button onclick="history.back()">Voltar</button>
         </body>
        </html>

     """

@app.get("/ordem-jogadores/", response_class=HTMLResponse)
async def definir_ordem(numero_Participantes: int = Query(...)):
    ordem_jogadores = []
    ordem2 = random.sample(range(1, numero_Participantes + 1), numero_Participantes)
    for i in range(numero_Participantes):
        ordem=ordem2[i]
        ordem_jogadores.append(f"<p> A ordem do jogador {i+1}: {ordem}° a jogar")
    return "".join(ordem_jogadores)


@app.get("/meus-territorios", response_class=HTMLResponse)
async def meus_territorios(numero_cor:int = Query(...)):
    território = receber_carta_território()
    return f"""
         <html>
            <head>Parabéns você recebeu o território : </head>
            <body>
                <h1>{território["Territorio"]}</h1>
                <form action ="/recebe-exercitos" method="get">
                <p> Digite seu id para receber seus exercitos </p>
                    <input type="number"id="numero_cor" name="numero_cor" required>
                    <button type="submit">Receber exercitos</button>
                 </form>
           <button onclick="history.back()">Voltar</button>
         </body>
        </html>
   """

@app.get("/recebe-exercitos", response_class=HTMLResponse)
async def recebe_exercitos(numero_cor:int= Query(...)):
    exercito = receber_exercito_inicial()
    return f"""
            <html>
            <head> </head>
            <body>
                <h2>{exercito["mensagem"]}</h2>
                <form action ="/meus-territorios/" method="get">
                    <p> Digite o nome do território que deseja colocar seu exercito</p>
                    <input type="text"id="nome_territorio" name="nome_territorio" required>
                    <p>Digite o valor do seu exercito</p>
                    <input type="number"id="valor_exercito" name="valor_exercito" required>
                    <button type="submit">Por exercito</button>
                </form>
           <button onclick="history.back()">Voltar</button>
         </body>
        </html>
    """

@app.get("/meus-territorios",response_class=HTMLResponse)
async def por_exercito(nome_território:str =Query(...),valor_exercito:int=Query(...)):
    
    colocarEXERCITO = colocar_exercito(nome_território, valor_exercito)
    return colocarEXERCITO

