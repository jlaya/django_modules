# -*- coding: utf-8 -*-
"""Vista."""
from pure_pagination.mixins import PaginationMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from django.urls import reverse
from .forms import SingupForm


class ProfileList(PaginationMixin, ListView):
    """Modelo ProfileList."""

    template_name = 'usercustom/list.html'
    model = User
    paginate_by = 10


class SingupView(CreateView):
    """SingupView."""

    model = User
    form_class = SingupForm
    initial = {'key': 'value'}
    template_name = 'usercustom/singup.html'

    def get(self, request, *args, **kwargs):
        """get."""
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """post."""
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_active = form.cleaned_data['is_active']
            p = User.objects.create_user(username=username,
                                         first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         is_active=is_active,
                                         password=password)
            p.save()
            return HttpResponseRedirect('/login')
        return render(request, self.template_name, {'form': form})


class ProfileDetail(DetailView):
    """ProfileDetail."""

    template_name = 'usercustom/detail.html'
    model = User
    paginate_by = 1


class ProfileUpdate(UpdateView):
    """ProfileUpdate."""

    template_name = 'usercustom/update.html'
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_success_url(self):
        """get_success_url."""
        return reverse('view_profiledetail', kwargs={'pk': self.object.pk})


class ProfileDelete(DeleteView):
    """ProfileDelete."""

    template_name = 'usercustom/delete.html'
    model = User
    success_url = reverse_lazy('list_users')
