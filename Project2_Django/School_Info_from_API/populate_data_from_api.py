import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'School_Info_from_API.settings')

import django
django.setup()

from school_basic.models import SchoolInfo
import requests


def add_data():
    res = requests.get("https://code.org/schools.json")
    data = res.json()
    schools = data['schools']

    for i in range(10):
        school_entry = SchoolInfo(name=schools[i]['name'], website=schools[i]['website'],
                                           languages=schools[i]['languages'], contact_number=schools[i]['contact_number'],
                                           city=schools[i]['city'], zip=schools[i]['zip'])
        school_entry.save()


if __name__ == '__main__':
    print("data population started")
    add_data()
    print("data population completed")
