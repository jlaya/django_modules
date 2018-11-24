from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import render


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "authentication/login.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
