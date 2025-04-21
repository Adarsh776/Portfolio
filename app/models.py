from django.db import models

# Create your models here.

class ProfileModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    resume = models.FileField(upload_to='resumes/',null=True, blank=True)
    social_links = models.JSONField(default=dict)  # e.g. {'github': 'link', 'linkedin': 'link'}
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class SkillModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_level = models.IntegerField()  # 1 to 10 scale

    def __str__(self):
        return f"{self.skill_name} - {self.skill_level}"

class ProjectModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = CloudinaryField('image', folder='projects', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200)  # e.g. Django, React, PostgreSQL
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

