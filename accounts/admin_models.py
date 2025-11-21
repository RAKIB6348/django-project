from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from accounts.models import User


class AdminProfile(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='admin_profile',
    )

    # YYMM1XXXX
    admin_user_id = models.IntegerField(
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated Admin ID (e.g., 250310001 → YYMM1XXXX)"
    )

    username = models.CharField(max_length=150, blank=True)

    # 👇 NEW FIELD ADDED HERE
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        help_text="Select gender"
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    # Address
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True, help_text="ZIP / Postal Code")
    country = models.CharField(max_length=100, default="Bangladesh", help_text="Country")

    profile_pic = models.ImageField(upload_to='admin_profiles/', blank=True, null=True)

    # Password fields
    password = models.CharField(max_length=128, blank=True, null=True)
    confirm_password = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Admin Profile'
        verbose_name_plural = 'Admin Profiles'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.admin_user_id or 'N/A'} - {self.first_name} {self.last_name}"

    def clean(self):
        if self.password and self.password != self.confirm_password:
            raise ValidationError("Password and Confirm Password do not match.")

    def save(self, *args, **kwargs):

        # Auto-generate admin_user_id
        if not self.admin_user_id:
            now = timezone.localtime()
            year_last_2 = now.strftime("%y")
            month_str = now.strftime("%m")

            prefix = f"{year_last_2}{month_str}1"
            start_range = int(f"{prefix}0001")
            end_range = int(f"{prefix}9999")

            last_admin = AdminProfile.objects.filter(
                admin_user_id__gte=start_range,
                admin_user_id__lte=end_range
            ).order_by('admin_user_id').last()

            if last_admin:
                new_number = (last_admin.admin_user_id % 10000) + 1
            else:
                new_number = 1

            self.admin_user_id = int(f"{prefix}{new_number:04d}")

        # Sync username
        if self.user and not self.username:
            self.username = self.user.username

        # Update user_id
        if hasattr(self.user, 'user_id') and not self.user.user_id:
            self.user.user_id = self.admin_user_id

        # Ensure admin role
        if hasattr(self.user, 'user_type') and self.user.user_type != 'Admin':
            self.user.user_type = 'Admin'

        # Handle password
        if self.password:
            self.user.set_password(self.password)
            self.password = None
            self.confirm_password = None

        if self.user:
            self.user.save()

        super().save(*args, **kwargs)
