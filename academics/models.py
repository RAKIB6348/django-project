from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.class_name}"
    


# ============ school session model ========================
class Session(models.Model):
    session_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_name
