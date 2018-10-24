from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SingupForm
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


class SingupView(CreateView):
    model = User
    form_class = SingupForm
    initial = {'key': 'value'}
    template_name = 'authentication/singup.html'

    def get(self, request, *args, **kwargs): 
        form = self.form_class(initial=self.initial) 
        return render(request, self.template_name, {'form': form}) 
 
    def post(self, request, *args, **kwargs): 
        form = self.form_class(request.POST) 
        if form.is_valid(): 
            username     = form.cleaned_data['username']
            first_name   = form.cleaned_data['first_name']
            last_name    = form.cleaned_data['last_name']
            email        = form.cleaned_data['email']
            password     = form.cleaned_data['password']
            is_active    = form.cleaned_data['is_active']

            p = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            p.save() 
            return HttpResponseRedirect('/login')
        return render(request, self.template_name, {'form': form})


# class UpdateProfile(UpdateView):
#     template_name = 'configuration/users/update.html'
#     model  = User
#     fields = ['username','first_name','last_name','email','is_active','company','address','phone','rif','provider','customer']
#     def get_success_url(self):
#         return reverse('detail_user', kwargs={'pk': self.object.pk,})


# class ChangePassword(UpdateView):
#     template_name = 'configuration/users/password_change.html'
#     form_class = ChangePasswordForm
#     model = User
#     fields = ['password']
#     initial = {'key': 'value'} 
    
#     def get(self, request, *args, **kwargs): 
#         form = self.form_class(initial=self.initial) 
#         return render(request, self.template_name, {'form': form}) 
 
#     def post(self, request, *args, **kwargs): 
#         form = self.form_class(request.POST) 
#         if form.is_valid():
#             user_id = User.objects.get(id=self.kwargs['pk'])
#             print user_id
#             user_id.password  = make_password(form.cleaned_data['password']) 
#             user_id.save()
#             return HttpResponseRedirect('/List_Users') 
 
#         return render(request, self.template_name, {'form': form})


# class DeleteUser(DeleteView):
#     template_name = 'configuration/users/delete.html' 
#     model = User
#     success_url = reverse_lazy('list_users')