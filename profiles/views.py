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
        'user': user,
        'profile': profile,
    })
