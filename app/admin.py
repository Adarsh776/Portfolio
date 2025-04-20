from django.contrib import admin
from .models import ProfileModel, SkillModel, ProjectModel, ContactModel
# Register your models here.

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone', 'address', 'resume', 'profile_image', 'social_links', 'bio')
    search_fields = ('name', 'email')
    list_filter = ('title',)
    ordering = ('name',)

@admin.register(SkillModel)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('profile', 'skill_name', 'skill_level')
    search_fields = ('skill_name',)
    list_filter = ('profile',)
    ordering = ('skill_name',)

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'github_link', 'live_demo_link', 'tech_stack', 'description', 'image')
    search_fields = ('title', 'tech_stack')
    list_filter = ('is_featured',)
    ordering = ('-is_featured',)

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_read',)
    ordering = ('-created_at',)
    actions = ['mark_as_read']

    # ✅ Admin action to mark messages as read
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"