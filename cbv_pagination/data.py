import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cbv_pagination.settings')
django.setup()
from PaginationApp.models import *
from faker import Faker
from random import *

fake=Faker()

def string_title(no):
    s = 'POST NO:- '+ str(no)
    return s

def generate_data(n):
    for i in range(1,n):
        title = string_title(i)
        author = fake.name()
        content = fake.text()

        obj = Posts.objects.get_or_create(title=title,author=author,content=content)


generate_data(21)