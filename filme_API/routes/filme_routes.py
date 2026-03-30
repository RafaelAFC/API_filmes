from flask import Blueprint, request

from controllers.filme_controller import create_filme, get_filmes

from controllers.filme_controller import create_filme

filme_routes = Blueprint('filme_routes', __name__)

@filme_routes.route('/filmes', methods=['POST'])
def filmes_post():
    return create_filme(request.json)

@filme_routes.route('/filmes', methods=['GET'])
def filmes_get():
    return get_filmes()