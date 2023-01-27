orders_len = 100

size_names = ['Personal', 'Medium', 'Familiar', 'XL', 'L\'ultima Cena']
ingredient_names = ['Salami', 'Pepperoni', 'Bacon', 'Extra Cheese',
                    'Meet', 'Tomato', 'Mushrooms', 'Pineapple', 'Onion', 'Corn']
beverage_names = ['Coca-Cola', 'Sprite', 'Fanta', 'Juice', 'Water']


def calculate_order_price(size_price: float, ingredients: list, beverages: list):
    price = sum(ingredient.price for ingredient in ingredients) + \
        sum(beverage.price for beverage in beverages) + size_price
    return round(price, 2)
