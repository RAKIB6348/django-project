from django.contrib import admin
from accounts.models import User
from accounts.admin_models import AdminProfile

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'user_id', 'user_type', 'email', 'date_joined']

    search_fields = ['username', 'user_id', 'user_type', 'email']

admin.site.register(User, UserAdmin)



class AdminProfileAdmin(admin.ModelAdmin):

    # list view column
    list_display = [
        'admin_user_id',
        'username',
        'first_name',
        'last_name',
        'gender',
        'email',
        'phone',
        'created_at',
    ]

    # search fields
    search_fields = [
        'admin_user_id',
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
        'user__username',   # search inside User model
        'user__user_id',
    ]

    # optional: ordering
    ordering = ['-created_at']


admin.site.register(AdminProfile, AdminProfileAdmin)

