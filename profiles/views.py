from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

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
    form = ProfileForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        avatar = request.method.POST.get('avatar')
        biography = request.method.POST.get('biography')

    return render(request, template_name, {
        'form': form,
    })
