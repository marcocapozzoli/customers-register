from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .forms import CustomPasswordResetForm, SignupForm, CustomAuthenticationForm, CustomSetPasswordForm


def dash(request):
    if request.user.is_authenticated:
        return render(request, "dash/home.html")
    else:
        return HttpResponseRedirect(reverse('login'))


class SignupView(CreateView):
    form_class = SignupForm
    # Indica para qual página será direcionada caso ocorra sucesso no cadastro
    success_url = reverse_lazy('login')
    # Informa para qual template é redirecionado caso a solicitação seja um get 
    template_name = 'users/signup.html'
    
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    pass


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset.html'
    success_url= reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
