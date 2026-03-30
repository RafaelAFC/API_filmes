from models.filme_models import Filme 
from db import db
import json
from flask import make_response

def create_filme(filme_data):
    novo_filme = Filme(
        titulo=filme_data['titulo'],
        genero=filme_data['genero'],
        duracao=filme_data['duracao'],
        ano_de_lancamento=filme_data['ano_de_lancamento'],
        diretor=filme_data['diretor']
    )
    db.session.add(novo_filme)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'filme cadastrado com sucesso.',
            'filme': novo_filme.json()
        }, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def get_filmes():
    filmes = Filme.query.all()
    response = make_response(
        json.dumps({
            'filmes': [filme.json() for filme in filmes]
        }, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response