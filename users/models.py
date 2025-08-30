from django.db import models
from django.contrib.auth.models import User

class Education(models.Model):
    job_seeker = models.ForeignKey('JobSeeker', on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Experience(models.Model):
    job_seeker = models.ForeignKey('JobSeeker', on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class JobSeeker(models.Model):
    # Basic Information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    # Personal & Contact Details
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    social_link_linkedin = models.JSONField(default=dict, blank=True)

    # Professional Profile
    summary = models.TextField(blank=True)
    skills = models.JSONField(default=list, blank=True)

    # Job Preferences & Application History
    desired_positions = models.JSONField(default=list, blank=True)
    desired_salary_range = models.JSONField(default=dict, blank=True)
    desired_locations = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.full_name
