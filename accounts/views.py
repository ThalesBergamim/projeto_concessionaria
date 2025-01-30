from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import RecoveryForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
import logging
from django.contrib.auth.hashers import make_password

logger = logging.getLogger(__name__)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            error_message = 'Usuário ou senha inválidos'
            login_form = AuthenticationForm()
            return render(request, 'login.html', {
                'login_form': login_form,
                'error_message': error_message
            })
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login')

def recovery_view(request):
    if request.method == 'POST':
        form = RecoveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            
            if user:
                try:
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    reset_url = request.build_absolute_uri(
                        f'/reset-password/{uid}/{token}/'
                    )
                    
                    context = {
                        'user': user,
                        'reset_url': reset_url
                    }
                    
                    email_html = render_to_string('password_reset_email.html', context)
                    email_text = render_to_string('password_reset_email.txt', context)
                    
                    send_mail(
                        'Recuperação de Senha',
                        email_text,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        html_message=email_html,
                        fail_silently=False,
                    )
                    
                    messages.success(request, 'Email de recuperação enviado com sucesso!')
                    return redirect('login')
                    
                except Exception as e:
                    messages.error(request, 'Erro ao processar a recuperação de senha.')
            else:
                messages.error(request, 'Email não encontrado.')
    else:
        form = RecoveryForm()
    
    return render(request, 'recovery.html', {'form': form})

def reset_password_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                password = request.POST.get('password')
                password2 = request.POST.get('password2')
                
                if password and password2:
                    if password == password2:
                        user.set_password(password)
                        user.save()
                        messages.success(request, 'Senha alterada com sucesso! Faça login com sua nova senha.')
                        return redirect('login')
                    else:
                        messages.error(request, 'As senhas não coincidem.')
                else:
                    messages.error(request, 'Preencha todos os campos.')
            
            return render(request, 'reset_password.html')
        else:
            messages.error(request, 'Link de recuperação inválido ou expirado.')
            return redirect('recovery')
            
    except Exception as e:
        messages.error(request, 'Erro ao processar a requisição.')
        return redirect('recovery')