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
from flask import Flask, jsonify, request
App = Flask(__name__)

Cores = [
    {
        'id':1,
        'Cor': "Azul",
    },
    {
        'id':2,
        'Cor': "Branca",
        
    },

    {
        'id':3,
        'Cor': "Vermelha",
       
        
    },

    {
        'id':4,
        'Cor': "Preta",
        
        
    },
    {
        'id':5,
        'Cor': "Amarela",
       
        
    },

    {
        'id':6,
        'Cor': "Verde",
        
    },

]

Objetivos=[ 
    {
        'id':1,
        'Objetivos':'Conquistar na totalidade a EUROPA, a OCEANIA e mais um terceiro.'
    },

    {
        'id':2,
         'Objetivos':' Conquistar na totalidade a ÁSIA e a AMÉRICA DO SUL.'
    },

    {
        'id':3,
        'Objetivos' :' Conquistar na totalidade a EUROPA, a AMÉRICA DO SUL e mais um terceiro.'
    },

    {
        'id':4,
        'Objetivos':'Conquistar 18 TERRITÓRIOS e ocupar cada um deles com pelo menos dois exércitos.'
    },

    {
        'id':5,
       'Objetivos' :'Conquistar na totalidade a ÁSIA e a ÁFRICA.'
    },

    {
        'id':6,
        'Objetivos':' Conquistar na totalidade a AMÉRICA DO NORTE e a ÁFRICA.'
    },

    {
        'id':7,
        'Objetivos':'Conquistar 24 TERRITÓRIOS à sua escolha.'
    },

    {
        'id':8,
        'Objetivos':'Conquistar na totalidade a AMÉRICA DO NORTE e a OCEANIA.'
    },

    {
        'id':9,
        'Objetivos':'Destruir totalmente OS EXÉRCITOS AZUIS.'
    },

    {
        'id':10,
        'Objetivos':' Destruir totalmente OS EXÉRCITOS AMARELOS.'
    }, 

    {
        'id':11,
        'Objetivos':'Destruir totalmente OS EXÉRCITOS VERMELHOS.'
    },

    {
        'id':12,
        'Objetivos':' Destruir totalmente OS EXÉRCITOS PRETOS.'
    },

    {
        'id':13,
        'Objetivos':'Destruir totalmente OS EXÉRCITOS BRANCO.'
    },

    {
        'id':14,
        'Objetivos':'Destruir totalmente OS EXÉRCITOS VERDES'
    }

]

#Consultar Cor
@App.route('/Cores',methods=['GET']) 
def obter_Cor():
    print("Digite a cor que deseja usar : ")
    return jsonify(Cores)  
App.run(port=5000, host='localhost', debug=True)

#Consultar
