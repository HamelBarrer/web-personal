from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms import UserForm

from .models import Profile
from .forms import ProfileForm


@login_required(login_url='users:login')
def profile_view(request):
    template_name = 'profiles/profil.html'
    user = request.user
    profile = Profile.objects.filter(user=user).first()

    return render(request, template_name, {
        'profile': profile,
    })


@login_required(login_url='users:login')
def edit_view(request, id):
    template_name = 'profiles/snippets/edit_profile.html'

    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(
        request.POST, request.FILES, instance=profile)
    user_form = UserForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, f'La informacion del perfil a sido modificada')
            return redirect('profiles:profil')

    return render(request, template_name, {
        'profile_form': profile_form,
        'user_form': user_form,
    })
