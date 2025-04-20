from django.urls import path
from .views import ProfileView, ProjectView, ContactView

urlpatterns = [
    path('', ProfileView.as_view(), name='overview'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]