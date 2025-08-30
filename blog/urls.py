from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    home,
    about
)

urlpatterns = [
    # Home y About
    path('', home, name='home'),
    path('about/', about, name='about'),

    # Listado de posts
    path('posts/', PostListView.as_view(), name='post_list'),

    # Detalle de post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Crear post (solo logueados)
    path('posts/new/', PostCreateView.as_view(), name='post_create'),

    # Editar post (solo logueados y autor)
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),

    # Eliminar post (solo logueados y autor)
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
