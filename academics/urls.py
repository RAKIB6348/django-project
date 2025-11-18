from django.urls import path
from academics.views import *


urlpatterns = [
    path('add-class/', add_class, name='add_class'),
]
