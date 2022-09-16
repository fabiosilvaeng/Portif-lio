from os import times
from flask import request,jsonify
import function as func
from random import randint as rd
jogos = {
    'megasena' : [(6,15),(1,60)],
    'lotofacil' : [(15,18),(1,25)],
    'quina' : [(5,15),(1,80)],
    'lotomania' : [(50,50),(0,99)],
    'timemania' : [(10,10),(1,80)],
    'duplasena': [(6,15),(1,50)]
}

def verify_mega():
    json_receive = request.get_json()
    number_per_game = {}

    for i in json_receive:
        if json_receive[i] >= jogos[i][0][0] and json_receive[i] <= jogos[i][0][-1]:
            number_per_game[i] = func.numbers(json_receive[i],jogos[i][-1],rd(1,80) if i == 'timemania' else '')
        else:
            msg = {'message': f'A quantidade de números solicitados para o jogo {i.upper()} não é permitida, por favor reenvie a quantidade de números correta.'}
            return jsonify(msg),500
    return jsonify(number_per_game),200




