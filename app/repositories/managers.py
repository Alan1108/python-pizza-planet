from typing import Any, List, Optional, Sequence
import calendar

from sqlalchemy.sql import text, column, func, desc, select

from app.singleton import SingletonMeta

from .models import (Ingredient, Order, IngredientsDetail,
                     BeveragesDetail, Size, db, Beverage)
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)


class BaseManager(metaclass=SingletonMeta):
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager, metaclass=SingletonMeta):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager, metaclass=SingletonMeta):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager, metaclass=SingletonMeta):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((IngredientsDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((BeveragesDetail(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @ classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager, metaclass=SingletonMeta):

    @ classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class BeverageManager(BaseManager, metaclass=SingletonMeta):
    model = Beverage
    serializer = BeverageSerializer

    @ classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class ReportManager(BaseManager, metaclass=SingletonMeta):
    session = db.session
    needed_clients = 3
    ingredient_detail = IngredientsDetail
    ingredient = Ingredient
    order = Order

    @ classmethod
    def get_most_requested_ingredient(cls):
        qry = cls.session.query(cls.ingredient_detail.ingredient_id, func.count(cls.ingredient_detail._id).label(
            'qty')).group_by(cls.ingredient_detail.ingredient_id).order_by(desc('qty')).first()
        complete_ingredient = cls.ingredient.query.get(qry.ingredient_id)
        return({
            'name': complete_ingredient.name,
            'quantity': qry.qty
        })

    @ classmethod
    def get_most_valuable_clients(cls):
        clients = cls.session.query(cls.order.client_name, func.count(cls.order.client_name).label(
            'qty')).group_by(cls.order.client_name).order_by(desc('qty')).limit(3).all()
        return [{
            'client_name': client.client_name
        }
            for client in clients
        ]

    @ classmethod
    def get_month_with_most_revenue(cls):
        month = cls.session.query(
            func.strftime('%m', cls.order.date).label('month'),
            func.sum(cls.order.total_price).label('total')).group_by('month').order_by(desc('total')).first()
        return {'month': calendar.month_name[int(month[0])], 'total': round(month[1], 2)}

    @ classmethod
    def get_report(cls):
        return{
            'most_requested_ingredient': cls.get_most_requested_ingredient(),
            'month_with_most_revenue': cls.get_month_with_most_revenue(),
            'most_valuable_clients': cls.get_most_valuable_clients()
        }
