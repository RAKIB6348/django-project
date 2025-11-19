from django.urls import path
from academics.views import *
from academics.session_views import *


urlpatterns = [
    path('add-class/', add_class, name='add_class'),
    path('class-list/', class_list, name='class_list'),

    # session urls
    path('add-session/', add_session, name='add_session'),
    path('session-list/', session_list, name='session_list'),
]
