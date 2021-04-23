from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'blog/post/post_list.html'
    ordering = ('-id')

    def get_context_data(self, *args, object_list=None, **kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cats_menu'] = cats_menu
        return context


class PostDetailView(DetailView):
    DetailView.model = Post
    template_name = 'blog/post/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/add_post.html'


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'blog/post/add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/post/upate_post.html'
    fields = ('title', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post/delete_post.html'
    success_url = reverse_lazy('blog:post_list')


def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    context = {
        'category_posts': category_posts,
        'cats': cats
    }
    return render(request, 'blog/post/category.html', context,)


def category_list_view(request):
    cats_list = Category.objects.all()
    context = {'cats_list': cats_list}
    return render(request, 'blog/post/category_list.html', context)