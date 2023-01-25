from ..repositories.managers import SizeManager
from .base import BaseController
from ..singleton import SingletonMeta


class SizeController(BaseController, metaclass=SingletonMeta):
    manager = SizeManager
