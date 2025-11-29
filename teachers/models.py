from django.db import models
from accounts.models import User


class TeacherInformation(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Resigned", "Resigned"),
        ("Suspended", "Suspended"),
        ("Retired", "Retired"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type' : 'Teacher'},
        related_name="teacher_info"
    )

    teacher_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        blank=True,
        null=True,
        help_text="Auto generated Teacher ID"
    )

    # Basic Information
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    blood_group = models.CharField(max_length=6, blank=True, null=True)

    # Job / Employment details
    designation = models.CharField(max_length=100, help_text="Example: Senior Teacher / Assistant Teacher")
    teacher_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Address Info
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=120, default="Bangladesh")

    # Documents
    profile_image = models.ImageField(upload_to="teachers/profile/", blank=True, null=True)
    nid_number = models.CharField(max_length=20, blank=True, null=True)
    certificate_file = models.FileField(upload_to="teachers/certificates/", blank=True, null=True)

    # Status + Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
