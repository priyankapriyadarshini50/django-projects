import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')


import django
django.setup()

# populate Fake Data
import random
from first_app.models import AccessRecord, WebPage, Topic
from faker import Faker

fake_obj = Faker()
topic_list = ['Social', 'Search', 'Game', 'News', 'Marketplace']


# Topic names are created to Topic table/schema as top_name field
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic_list))[0]
    t.save()
    return t


def populate_fake_data(n=5):
    for entry in range(n):

        # get the Topic for the entry
        top = add_topic()

        # Create Fake data for each field
        fake_url = fake_obj.url()
        fake_date = fake_obj.date()
        fake_name = fake_obj.company()

        # create the Webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # create a AccessRecord entry for Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating Scripts!')
    populate_fake_data()
    print("populating fake data completed.")








