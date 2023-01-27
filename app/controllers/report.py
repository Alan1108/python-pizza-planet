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
