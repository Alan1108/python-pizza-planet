from flask_seeder import Faker, generator
from faker import Faker as fk
from random import randint
import datetime
from app.repositories.models import *
from app.test.utils.functions import *


def gen_random_clients():
    fake = fk()
    client_counter = randint(5, 15)
    clients = []
    for i in range(client_counter):
        clients.append({
            'name': fake.name(),
            'dni': get_random_sequence(10),
            'address': fake.address(),
            'phone': fake.phone_number()
        })
    return clients


def gen_fake_order(order_id, total_price, size_id, client):
    fake = fk()
    return Faker(
        cls=Order,
        init={
            '_id': order_id,
            'client_name': client['name'],
            'client_dni': client['dni'],
            'client_address': client['address'],
            'client_phone': client['phone'],
            'date': fake.date_between(datetime.fromisoformat('2020-01-01'), datetime.fromisoformat(datetime.now().date().isoformat())),
            'total_price': total_price,
            'size_id': size_id
        }
    )


def gen_fake_items(item_type, item_class, id):
    return Faker(
        cls=item_class,
        init={
            '_id': id,
            'name': item_type,
            'price': get_random_price(1.5, 5)
        }
    )


def gen_fake_ingredients_detail(data: dict):
    return Faker(
        cls=IngredientsDetail,
        init={
            '_id': data['_id'],
            'ingredient_price': data['ingredient_price'],
            'order_id': data['order_id'],
            'ingredient_id': data['ingredient_id'],
        }
    )


def gen_fake_beverages_detail(data: dict):
    return Faker(
        cls=BeveragesDetail,
        init={
            '_id': data['_id'],
            'beverage_price': data['beverage_price'],
            'order_id': data['order_id'],
            'beverage_id': data['beverage_id'],
        }
    )


def list_item_maker(items, ClassType):
    items_created = []
    item_counter = 1
    for item in items:
        items_created.append(gen_fake_items(
            item, ClassType, item_counter).create()[0])
        item_counter += 1
    return items_created
