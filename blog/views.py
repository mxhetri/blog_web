from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
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

    def get_context_data(self,*args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        print('context value', context)
        return context


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
    form_class = EditForm
    template_name = 'blog/post/upate_post.html'


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


def post_like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    # request contains user id if logged in
    if post.likes.filter(id = request.user.id).exists():
        # user already liked, unlike now
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    # post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_detail', args=[str(pk)]))

