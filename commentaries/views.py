from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Commentarie

from .forms import CommentarieForm


class CommentarieListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = 'commentaries/commentarie.html'
    queryset = Commentarie.objects.all().order_by('-pk')
