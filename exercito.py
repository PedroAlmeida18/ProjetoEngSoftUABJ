
exercito = [
    {'id': 1, 'exercito': "Pequeno", 'valor': 1},
    {'id': 2, 'exercito': "Grande", 'valor': 10},
]

territorios_exercito = {}

def receber_exercito_inicial():
    return {"Mensagem": "Você recebeu 3 exercitos pequenosno valor de 1 cada",
            "Mensagem": "Escolha qual território vai colocá-los"
    }

def colocar_exercito(territorios: str, valor: int):
    if valor <= 0:
        return {'Menssgem': "Escolha um valor valido"}
    
    if territorios in territorios_exercito:
        territorios_exercito[territorios] += valor
    else:
        territorios_exercito[territorios] = valor
    return {
        "Mensagem": f"Colocados {valor} exércitos no território {territorios}.",
        "Territórios": territorios_exercito
    }    