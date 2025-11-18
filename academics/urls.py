from django.urls import path
from academics.views import *


urlpatterns = [
    path('add-class/', add_class, name='add_class'),
    path('class-list/', class_list, name='class_list'),
]
