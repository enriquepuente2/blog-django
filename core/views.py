from django.shortcuts import render
from django.views.generic import View

from boletininformativo.forms import NewsletterUserSignUpForm
from boletininformativo.models import NewsletterUser

from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
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
                message = EmailMessage(
                    subject, html_message, from_email, to_email)
                message.content_subtype = 'html'
                message.send()
            context = {
                'form': form,
            }
            return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'about.html', context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        message_name = request.POST['full_name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['mail@test.com'],
        )

        messages.success(request, 'Mensaje enviado correctamente')

        context = {

        }
        return render(request, 'contact.html', context)
