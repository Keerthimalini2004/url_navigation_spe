from django.urls import path
from shopping.views import*
app_name='shopping'

urlpattern5s=[
    path('suites/',suites,name='suites'),
]