from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # 🔹 Mensaje amigable si no es el autor
    def handle_no_permission(self):
        messages.error(self.request, "No puedes editar un post que no es tuyo.")
        return redirect('post_list')

    def get_success_url(self):
        messages.success(self.request, "Post actualizado correctamente.")  # mensaje de éxito
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # 🔹 Mensaje amigable si no es el autor
    def handle_no_permission(self):
        messages.error(self.request, "No puedes eliminar un post que no es tuyo.")
        return redirect('post_list')

    # 🔹 Mensaje de éxito al eliminar
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

