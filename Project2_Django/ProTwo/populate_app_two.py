import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
# go and populate the database
import django
django.setup()

from AppTwo.models import UsersInfo
from faker import Faker

fake_obj = Faker()


# FAKE POPULATION SCRIPT
def populate_fake_usersinfo(n=5):
    # Creates 5 rows in the database table
    for entry in range(n):
        # creates fake data for each row
        fake_name = fake_obj.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_obj.email()

        # creates a UserInfo table entry/row
        info = UsersInfo.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Data entry started")
    populate_fake_usersinfo(10)
    print("Data population completed.")
