import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
from second_project.second_app.models import UserInfo
from faker import Faker
import random


def add_data():
    fake_obj = Faker()
    fake_name = fake_obj.name().split()
    fake_fname = fake_name[0]
    fake_lname = fake_name[1]
    fake_email = fake_obj.email()
    fake_qalify = random.choice(['UG', 'G', 'PG', 'PhD'])

    user_obj = UserInfo.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email,
                                              qualification=fake_qalify)
    return user_obj


if __name__ == '__main__':
    print('Data populating')
    for i in range(5):
        print(add_data())
    print('Data population completed')
