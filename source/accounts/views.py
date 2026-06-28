from accounts.forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView


User = get_user_model()
class AuthLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

def logout_view(request):
    logout(request)

    return redirect('list_project')
class RegisterView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('list_project')
        return next_url
