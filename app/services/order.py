from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request
from .base_service import execute_service

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return execute_service(OrderController, POST, request.json)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return execute_service(OrderController, GET, _id)


@order.route('/', methods=GET)
def get_orders():
    return execute_service(OrderController, GET)
