from django.urls import path

from . import views

app_name = 'commentaries'
urlpatterns = [
    path('', views.CommentarieListView.as_view(), name='commentarie'),
]
