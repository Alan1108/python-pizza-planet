from flask_seeder import Seeder
from app.seeds.dataFaker import *
from random import choice, choices
from app.seeds.utils.utils import *
from app.repositories.models import *


class DBSeeder(Seeder):

    def save_data(self, data):
        for item in data:
            self.db.session.add(item)

    def run(self):
        sizes_created = list_item_maker(size_names, Size)
        ingredients_created = list_item_maker(ingredient_names, Ingredient)
        beverages_created = list_item_maker(beverage_names, Beverage)
        client_names = gen_random_clients()
        self.save_data(sizes_created)
        self.save_data(ingredients_created)
        self.save_data(beverages_created)
        created_orders = []
        ingredients_detail = []
        beverages_detail = []
        beverage_counter = 0
        ingredient_counter = 0
        for order_counter in range(1, orders_len+1):
            random_ingredients = choices(ingredients_created)
            random_beverages = choices(beverages_created)
            random_client = choice(client_names)
            random_size = choice(sizes_created)
            total_price = calculate_order_price(
                random_size.price, random_ingredients, random_beverages)
            created_orders.append(gen_fake_order(
                order_counter, total_price, random_size._id, random_client).create()[0])
            for ingredient in random_ingredients:
                ingredient_counter += 1
                aux_ingredient_detail = {
                    '_id': ingredient_counter,
                    'ingredient_price': ingredient.price,
                    'order_id': order_counter,
                    'ingredient_id': ingredient._id
                }
                ingredients_detail.append(gen_fake_ingredients_detail(
                    aux_ingredient_detail).create()[0])

            for beverage in random_beverages:
                beverage_counter += 1
                aux_beverage_detail = {
                    '_id': beverage_counter,
                    'beverage_price': beverage.price,
                    'order_id': order_counter,
                    'beverage_id': beverage._id
                }
                beverages_detail.append(gen_fake_beverages_detail(
                    aux_beverage_detail).create()[0])
            self.save_data(ingredients_detail)
            self.save_data(beverages_detail)
            ingredients_detail.clear()
            beverages_detail.clear()
        self.save_data(created_orders)
