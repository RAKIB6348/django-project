from django.contrib import admin
from .models import StudentInformation


@admin.register(StudentInformation)
class StudentInformationAdmin(admin.ModelAdmin):
    # লিস্ট ভিউতে যা দেখাবে
    list_display = (
        "admission_id",
        "student_user_id",
        "full_name",
        "class_name",
        "section",
        "session",
        "roll_number",
        "status",
        "created_at",
    )

    # ডান পাশে ফিল্টার
    list_filter = (
        "class_name",
        "section",
        "session",
        "status",
        "gender",
        "blood_group",
    )

    # সার্চ অপশন
    search_fields = (
        "first_name",
        "last_name",
        "student_user_id",
        "admission_id",
        "roll_number",
        "registration_no",
        "user__username",
        "user__email",
        "phone",
    )

    # কোন ফিল্ডগুলো শুধু read-only থাকবে
    readonly_fields = (
        "student_user_id",
        "admission_id",
        "admission_date",
        "created_at",
        "updated_at",
    )

    # ডিফল্ট অর্ডার
    ordering = ("-created_at",)

    # ফর্ম লেআউট একটু সাজানো
    fieldsets = (
        ("User & IDs", {
            "fields": ("user", "student_user_id", "admission_id"),
        }),
        ("Basic Profile", {
            "fields": (
                "first_name",
                "last_name",
                "phone",
                "email",
                "date_of_birth",
                "gender",
                "blood_group",
            ),
        }),
        ("Academic Information", {
            "fields": (
                "class_name",
                "section",
                "session",
                "roll_number",
                "registration_no",
                "admission_date",
            ),
        }),
        ("Guardian Information", {
            "fields": (
                "father_name",
                "mother_name",
                "guardian_phone",
                "guardian_email",
                "guardian_relation",
            ),
        }),
        ("Address", {
            "fields": (
                "address",
                "city",
                "district",
                "postal_code",
                "country",
            ),
        }),
        ("Documents", {
            "fields": (
                "profile_image",
                "birth_certificate",
                "id_card_no",
            ),
        }),
        ("Status & Tracking", {
            "fields": (
                "status",
                "created_at",
                "updated_at",
            ),
        }),
    )
