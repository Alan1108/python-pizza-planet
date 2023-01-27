from sqlalchemy.exc import SQLAlchemyError
from ..singleton import SingletonMeta
from .base import BaseController
from ..repositories.managers import ReportManager


class ReportController(BaseController, metaclass=SingletonMeta):
    manager = ReportManager

    @ classmethod
    def get(cls):
        try:
            return cls.manager.get_report(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_most_requested_ingredient(cls):
        try:
            return cls.manager.get_most_requested_ingredient(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_month_with_most_revenue(cls):
        try:
            return cls.manager.get_month_with_most_revenue(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_most_valuable_clients(cls):
        try:
            return cls.manager.get_most_valuable_clients(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
