from django.contrib import admin
from academics.models import SchoolClass, Session

# Register your models here.
class SchoolClassAdmin(admin.ModelAdmin):

    list_display = ['class_name', 'class_code', 'created_at']

    search_fields = ['class_name', 'class_code']

admin.site.register(SchoolClass, SchoolClassAdmin)



# ================= session ====================
class SchoolSessionAdmin(admin.ModelAdmin):

    list_display = ['session_name', 'start_date', 'end_date','created_at']

    search_fields = ['session_name']


admin.site.register(Session, SchoolSessionAdmin)
