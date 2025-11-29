from django.urls import path
from academics.views import *
from academics.session_views import *
from academics.subject_views import *
from academics.section_views import *


urlpatterns = [
    path('add-class/', add_class, name='add_class'),
    path('class-list/', class_list, name='class_list'),

    # session urls
    path('add-session/', add_session, name='add_session'),
    path('session-list/', session_list, name='session_list'),


    # subject urls
    path('add-subject/', add_subject_page, name='add_subject_page'),
    path('subject-list/', list_subject_page, name='list_subject_page'),


    # section urls
    path('add-section/', add_section, name='add_section'),
]
