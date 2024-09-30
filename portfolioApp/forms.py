from django import forms
from .models import ContactFormDetails

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormDetails
        fields = ['name', 'email', 'subject', 'message']  # Ensure these fields match your model exactly
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject*'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message*', 'rows': 8}),
        }
