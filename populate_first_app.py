import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

## FACKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
  t.save()
  return t

def populate(N=5):
  for entry in range(N):
    # get topic for the entry
    top = add_topic()

    # create fake data for that entry
    fake_url = fakegen.url()
    fake_name = fakegen.company()

    # create new web page entry
    webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

    fake_date = fakegen.date()
    # create fake access record
    access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
  print("populating script!")
  populate(1)
  print('populating compleate!')

## To run it
# python populate_first_app.py
