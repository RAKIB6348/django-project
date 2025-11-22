from django.urls import path
from accounts.views import *
from accounts.admin_views import *
from accounts.profile_views import *



urlpatterns = [

    # base urls
    path('dashboard/', dashboard_page, name='dashboard_page'),


    #login urls
    path('', login_page,  name='login_page'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name="user_logout"),

    # admin register
    path('register/admin/', register_admin, name='register_admin'),
    path('admin-list/', admin_list_page, name="admin_list_page"),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),


    # profile
    path('profile/', view_profile_page, name='view_profile_page'),
]
