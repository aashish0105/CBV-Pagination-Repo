from django.urls import path
from .views import *
urlpatterns=[
    path('displaygen/',PostsListViewGen.as_view(),name='displaygen'),
    path('display/',PostsListView.as_view(),name='display')
]