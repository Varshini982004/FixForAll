from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):

    ISSUE_TYPES = [
        ('pothole', 'Pothole / Road Damage'),
        ('streetlight', 'Broken Streetlight'),
        ('garbage', 'Garbage / Waste'),
        ('water', 'Water Leakage'),
        ('drainage', 'Drainage Problem'),
        ('infrastructure', 'Damaged Public Infrastructure'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('verified', 'Verified'),
        ('assigned', 'Department Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    DEPARTMENT_CHOICES = [
        ('electricity', 'Electricity Department'),
        ('roads', 'Roads & Infrastructure Department'),
        ('sanitation', 'Sanitation Department'),
        ('water', 'Water Department'),
        ('drainage', 'Drainage Department'),
        ('municipal', 'Municipal Department'),
        ('other', 'Other Department'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    issue_type = models.CharField(
        max_length=30,
        choices=ISSUE_TYPES
    )

    location = models.CharField(max_length=300)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='submitted'
    )

    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title