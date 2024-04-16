from django.urls import path

from .views import newsletter_signup, newsletter_unsubscribe

app_name = "boletininformativo"

urlpatterns = [
    path('signup/', newsletter_signup, name="signup"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),
]
