from flask import jsonify, request, Request
from typing import Optional
from app.common.http_methods import *


def execute_service(Controller, method, request: Optional[Request] = None, id: Optional[int] = None, isReportService: Optional[bool] = False):
    entity, error = Controller.create(request) if method == POST \
        else Controller.update(request) if method == PUT \
        else Controller.get_by_id(id) if id \
        else Controller.get_all() if method == GET and not isReportService \
        else Controller.get()
    response = entity if not error else {'error': error}
    status_code = 200 if entity else 404 if not error else 400
    return jsonify(response), status_code
