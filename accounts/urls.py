from django.urls import path
from accounts.views import *
from accounts.admin_views import *

urlpatterns = [

    # base urls
    path('dashboard/', dashboard_page, name='dashboard_page'),


    #login urls
    path('', login_page,  name='login_page'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name="user_logout"),

    # admin register
    path('register/admin/', register_admin, name='register_admin'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
]
