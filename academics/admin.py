from django.contrib import admin
from academics.models import SchoolClass

# Register your models here.
class SchoolClassAdmin(admin.ModelAdmin):

    list_display = ['class_name', 'class_code', 'created_at']

    search_fields = ['class_name', 'class_code']

admin.site.register(SchoolClass, SchoolClassAdmin)
