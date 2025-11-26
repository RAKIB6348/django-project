from django.contrib import admin
from academics.models import SchoolClass, Session, Subject, Section

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



# ==================== subject ======================
class SchoolSubjectAdmin(admin.ModelAdmin):

    list_display = ['subject_name', 'subject_code', 'created_at']

    search_fields = ['subject_name', 'subject_name']

admin.site.register(Subject, SchoolSubjectAdmin)



# =================== section =========================
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'created_at']
    search_fields = ['section_name']

admin.site.register(Section, SectionAdmin)
