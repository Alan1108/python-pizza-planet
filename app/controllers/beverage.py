from ..repositories.managers import BeverageManager
from .base import BaseController
from ..singleton import SingletonMeta


class BeverageController(BaseController, metaclass=SingletonMeta):
    manager = BeverageManager
