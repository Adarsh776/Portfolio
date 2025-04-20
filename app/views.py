from django.shortcuts import render,redirect
from .models import ProfileModel, SkillModel, ProjectModel, ContactModel
from django.views import View
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

class ProfileView(View):
    def get(self, request):
        profile = ProfileModel.objects.first()
        skills = SkillModel.objects.all()
        projects = ProjectModel.objects.all()
        return render(request, 'index.html', {'profile': profile, 'skills': skills, 'projects': projects})

class ProjectView(View):
    def get(self, request):
        projects = ProjectModel.objects.all()
        return render(request, 'projects.html', {'projects': projects})

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # ✅ Send email notification to yourself
            subject = "New Contact Form Submission"
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Subject: {form.cleaned_data['subject']}
            Message: {form.cleaned_data['message']}
            """
            from_email = form.cleaned_data['email']

            send_mail(subject, message, from_email, ["adarshadi7760@gmail.com"])  # update recipient

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # or a thank you page

        return render(request, 'contact.html', {'form': form})

 

def custom_404(request, exception):
    return render(request, '404.html', status=404)