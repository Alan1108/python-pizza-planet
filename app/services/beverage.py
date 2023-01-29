from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base_service import execute_service

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return execute_service(BeverageController, POST, request.json)


@beverage.route('/', methods=PUT)
def update_beverage():
    return execute_service(BeverageController, PUT, request.json)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return execute_service(BeverageController, GET, _id)


@beverage.route('/', methods=GET)
def get_all():
    return execute_service(BeverageController, GET)
