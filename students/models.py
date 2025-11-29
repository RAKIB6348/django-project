from django.db import models
from accounts.models import User
from academics.models import SchoolClass, Section, Session


class StudentInformation(models.Model):
    BLOOD_GROUP = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Leave', 'Leave'),
        ('Suspended', 'Suspended'),
        ('Passed Out', 'Passed Out'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_info",
        limit_choices_to={'user_type' : 'Student'}
    )

    student_user_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        blank=True,
        null=True,
        help_text="Auto Student System ID"
    )

    admission_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        blank=True,
        null=True,
        help_text="Auto generated admission ID"
    )

    # Basic Profile
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=20,
        blank=True,
        null=True,
    )
    blood_group = models.CharField(
        choices=BLOOD_GROUP,
        max_length=5,
        blank=True,
        null=True,
    )

    # Academic Information
    roll_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Institute-wise roll or internal student code.",
    )
    registration_no = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text="Board/official registration no.",
    )

    class_name = models.ForeignKey(
        SchoolClass,
        on_delete=models.PROTECT,
        related_name="students",
    )  # e.g. Class 6, 7, 8
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="students",
        blank=True,
        null=True,
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.PROTECT,
        related_name="students",
    )  # e.g. 2024-2025

    admission_date = models.DateField(auto_now_add=True)

    # Guardian Information
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(blank=True, null=True)
    guardian_relation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Father / Mother / Uncle etc.",
    )

    # Address
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, default="Bangladesh")

    # Documents
    profile_image = models.ImageField(
        upload_to="students/profile/",
        blank=True,
        null=True,
    )
    birth_certificate = models.FileField(
        upload_to="students/docs/",
        blank=True,
        null=True,
    )

    id_card_no = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text="Internal ID card number.",
    )

    # Tracking
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Students Information"
        ordering = ["-created_at"]
        # Roll unique inside session+class+section
        constraints = [
            models.UniqueConstraint(
                fields=["session", "class_name", "section", "roll_number"],
                name="unique_roll_per_class_section_session",
            ),
        ]

    def __str__(self):
        roll = self.roll_number or "No Roll"
        return f"{self.first_name} {self.last_name} ({roll})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
