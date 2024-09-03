cores = [
    {'id': 1, 'Cor': "Azul"},
    {'id': 2, 'Cor': "Branca"},
    {'id': 3, 'Cor': "Vermelha"},
    {'id': 4, 'Cor': "Preta"},
    {'id': 5, 'Cor': "Amarela"},
    {'id': 6, 'Cor': "Verde"},
]


def escolha_cor(cor: int):
    if cor < 1 or cor > len(cores):
        return {"Faça uma escolha valida. Cor do Exército : 1-Azul, 2-Branca, 3-Vermelha, 4-Preta, 5-Amarela, 6-Verde"}
    
    cor_jogador = cores[cor -1]
    return { "Mensagem": "Parabéns você escolheu uma cor", 
                "Cor": cor_jogador['Cor'],
                "Mensagem2": "Após escolher a cor, vá para a rota /receber-objetivo/ e receba seu objetivo"}

