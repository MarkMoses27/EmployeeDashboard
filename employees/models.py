from django.db import models

# Create your models here.
# employees/models.py
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    # Add more fields as needed


def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id}) - Email: {self.email}, Phone: {self.phone_number}, Department: {self.department}"