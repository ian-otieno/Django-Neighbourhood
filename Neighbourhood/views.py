from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from Neighbourhood.models import Business, Membership, NeighbourHood, Post, Profile
from .forms import AddBussinessForm, AddNeighbourhoodForm, AddPostForm, PasswordChangeForm, UpdateProfileForm, UpdateUserForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from Core import settings
import threading

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate Your Neighbourhood Account'
    email_body = render_to_string('Account Activation Email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
    from_email=settings.EMAIL_FROM_USER, to=[user.email])

    if not settings.TESTING:
        EmailThread(email).start()

def Register(request):
    if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Already Exists! Choose Another One')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists! Choose Another One')
            return redirect('Register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.is_active = False
        user.save()

        if not context['has_error']:
            send_activation_email(user, request)
            messages.success(request, '✅ Regristration Successful! An Activation Link Has Been Sent To Your Email')
            return redirect('Register')

    return render(request, 'Register.html')

