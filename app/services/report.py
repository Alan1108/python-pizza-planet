from app.common.http_methods import GET
from flask import Blueprint
from .base_service import execute_service

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return execute_service(ReportController, GET, isReportService=True)
