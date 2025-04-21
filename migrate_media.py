import os
import sys
import django
from pathlib import Path

# Add the project root directory to the Python path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import cloudinary.uploader
from django.core.files.storage import default_storage
from app.models import ProfileModel, ProjectModel

def migrate_profile_images():
    profiles = ProfileModel.objects.all()
    for profile in profiles:
        if profile.profile_image and hasattr(profile.profile_image, 'path'):
            try:
                # Upload to Cloudinary
                result = cloudinary.uploader.upload(
                    profile.profile_image.path,
                    folder='profile_images'
                )
                # Update the model with Cloudinary URL
                profile.profile_image = result['secure_url']
                profile.save()
                print(f"Migrated profile image for {profile.name}")
            except Exception as e:
                print(f"Error migrating profile image for {profile.name}: {str(e)}")

def migrate_project_images():
    projects = ProjectModel.objects.all()
    for project in projects:
        if project.image and hasattr(project.image, 'path'):
            try:
                # Upload to Cloudinary
                result = cloudinary.uploader.upload(
                    project.image.path,
                    folder='projects'
                )
                # Update the model with Cloudinary URL
                project.image = result['secure_url']
                project.save()
                print(f"Migrated project image for {project.title}")
            except Exception as e:
                print(f"Error migrating project image for {project.title}: {str(e)}")

if __name__ == "__main__":
    print("Starting media migration to Cloudinary...")
    migrate_profile_images()
    migrate_project_images()
    print("Media migration completed!") 