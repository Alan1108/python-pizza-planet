from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base_service import execute_service

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return execute_service(IngredientController, POST, request.json)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return execute_service(IngredientController, PUT, request.json)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return execute_service(IngredientController, GET, _id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return execute_service(IngredientController, GET)
