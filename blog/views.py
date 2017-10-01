from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Predio, Agendamento
from django.shortcuts import render, get_object_or_404
# from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .filters import TitleFilter
import datetime
from datetime import timedelta

now = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S')


def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html') #, {'posts': posts}

@login_required
def home(request):
    now2 = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S')
    time = datetime.datetime.now().time()
    agendamentos = Agendamento.objects.filter(date=timezone.now(), on__lte=time, off__gte=time)
    a = []
    for agendamento in agendamentos:
        a.append(agendamento.predio.pk)
    predios_on = Predio.objects.filter(pk__in=a)
    predios_off= Predio.objects.all().exclude(pk__in=a)
    return render(request, 'blog/home.html', {'now2':now2, 'agendamentos': agendamentos, 'predios_on': predios_on, 'predios_off': predios_off, 'time': time} )


# def search(request):
#     post_list = Post.objects.all()
#     post_filter = TitleFilter(request.GET, queryset=post_list)
#     return render(request, 'blog/search.html', {'filter': post_filter})
#
#def authors(request, pk):
#    me = get_object_or_404(Post, pk=pk)
#    posts = Post.objects.filter(author=me)
    # user = Post.objects.get(Post, username=author)
    # post = Post.objects.filter(author=user)
#    return render(request, 'blog/authors.html', {'posts': posts})
#
# def authors(request):
#      me = User.objects.get(username=request.user)
#      posts = Post.objects.filter(author=me)
#     # user = Post.objects.get(Post, username=author)
#     # post = Post.objects.filter(author=user)
#      return render(request, 'blog/authors.html', {'posts': posts})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
# @login_required
# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
#
# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
#
# @login_required
# def post_remove(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post_list')
#
# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
#
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})
#
# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)
#
def about(request):
    return render(request, 'blog/about.html', {})
