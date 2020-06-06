from django.shortcuts import render
from django.views.generic import View

from .models import Profile
from .forms import ProfileForm


def profile_view(request):
    template_name = 'profiles/profil.html'
    user = request.user
    profile = Profile.objects.filter(user=user).first()

    return render(request, template_name, {
        'profile': profile,
    })
