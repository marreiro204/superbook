# posts/urls.py
from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path("", views.index, name="index"),
    path('lista/', views.lista_posts, name='lista_posts'),
    path("cbv-lista/", views.PostListView.as_view(), name="cbv_lista_posts"),
    path("novo/", views.criar_post, name="criar_post"),
]
