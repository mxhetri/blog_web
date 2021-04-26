from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UpdateProfileForm, UserPasswordChangeForm
from blog.models import Profile
# Create your views here.


class UserRegistrationView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('blog:post_list')


class UserEditView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog:post_list')

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/user_password_change_done.html'
    success_url = reverse_lazy('blog:post_list')


class UserProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    # extract user profile suing pk of user
    def get_context_data(self, *args, object_list=None, **kwargs):
        # user = Profile.objects.all()
        user_detail = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(UserProfilePageView, self).get_context_data(*args, **kwargs)
        context['user_detail'] = user_detail
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ('bio','profile_pic', 'website_url', 'facebook_url', 'twitter_url')
    success_url = reverse_lazy('blog:post_list')


