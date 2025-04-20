from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your message here...'}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }
        error_messages = {
            'name': {
                'required': "Please enter your name.",
            },
            'email': {
                'required': "Please enter a valid email address.",
                'invalid': "Invalid email format.",
            },
            'subject': {
                'required': "Please enter a subject.",
            },
            'message': {
                'required': "Please enter your message.",
            },
        }