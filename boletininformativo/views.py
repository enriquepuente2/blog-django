from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from boletininformativo.models import NewsletterUser
from .forms import NewsletterUserSignUpForm

# Create your views here.

# Logica para mandar mensaje cuando el usuario hace signup en el formulario


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        isinstance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=isinstance.email).exists():
            messages.warning(request, 'Email already exists.')

        else:
            isinstance.save()
            messages.success(
                request, 'Hemos enviado un correo electronico a su correo, abrelo para continuar con el entrenamiento')
            # Correo electronico
            subject = "Libro de cocina"
            from_email = settings.EMAIL_HOST_USER
            to_email = [isinstance.email]

            html_template = 'newsletters/email_templates/welcome.html'
            html_message = render_to_string(html_template)
            message = EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype = 'html'
            message.send()
    context = {
        'form': form,
    }
    return render(request, 'start-here.html', context)


# Logica para mandar mensaje cuando el usuario hace eliminacion de usuario en el formulario
def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        isinstance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=isinstance.email).exists():
            NewsletterUser.objects.filter(email=isinstance.email).delete()
            messages.success(request, 'Email has been removed.')
        else:
            print('Email not found.')
            messages.warning(request, 'Email not found.')

    context = {
        'form': form,
    }
    return render(request, 'unsubscribe.html', context)
