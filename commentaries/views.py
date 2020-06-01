from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Profile

from .models import Commentarie

from .forms import CommentarieForm


class CommentarieListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = 'commentaries/commentarie.html'
    queryset = Commentarie.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context['profile'] = profile
        return context


class CommentarieCreateView(CreateView):
    template_name = 'commentaries/add_commentarie.html'
    model = Commentarie
    form_class = CommentarieForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('commentaries:commentarie')
