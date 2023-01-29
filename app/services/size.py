from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .base_service import execute_service

from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return execute_service(SizeController, POST, request.json)


@size.route('/', methods=PUT)
def update_size():
    return execute_service(SizeController, PUT, request.json)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return execute_service(SizeController, GET, _id)


@size.route('/', methods=GET)
def get_all():
    return execute_service(SizeController, GET)
