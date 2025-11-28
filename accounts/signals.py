from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    subject = "Welcome to VoxelEngine!"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    # Load the HTML template
    html_content = render_to_string('account/email/welcome_email.html', {'user': user})
    
    # Create the email
    msg = EmailMultiAlternatives(subject, "Welcome to VoxelEngine! We are glad to have you.", from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
