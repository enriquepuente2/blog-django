from django import forms

from .models import Newsletter, NewsletterUser

# Creacion de formularios


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'subject', 'body', 'email', 'status']
