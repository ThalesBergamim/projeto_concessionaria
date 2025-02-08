from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def send_recovery_email(user):

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    recovery_link = f"{settings.SITE_URL}/accounts/reset-password/{uid}/{token}/"

    context = {
        'user': user,
        'recovery_link': recovery_link
    }

    html_message = render_to_string('accounts/email/password_reset_email.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        'Recuperação de Senha',
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )
