from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
# Create your views here.


class UserRegistrationView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('blog:post_list')


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog:post_list')

    def get_object(self):
        return self.request.user
