from ..repositories.managers import IngredientManager
from .base import BaseController
from ..singleton import SingletonMeta


class IngredientController(BaseController, metaclass=SingletonMeta):
    manager = IngredientManager
