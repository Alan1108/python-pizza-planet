from faker import Faker
from app.repositories.models import *
from app.test.utils.functions import get_random_sequence

fake = Faker()


class GenFakeData():

    def gen_client_data():
        name = fake.name()
        address = fake.address()
        phone = fake.phone_number()
        dni = get_random_sequence(10)
        date = fake.date_between(start_date=datetime.fromisoformat(
            '2020-01-01'), end_date=datetime.now())
        print(date)
        fake.date_between(start_date=datetime.fromisoformat(
            '2020-01-01'), end_date=datetime.now())


faker = GenFakeData()
faker.gen_client_data()
