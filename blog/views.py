from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.core.context_processors import csrf
from django.contrib.auth import logout,get_user
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# Create your views here.
from blog.forms import PostForm,CommentForm
from models import Post
from django.contrib.auth.models import User

@login_required
def index(request):
    posts = Post.objects.all()

    return render_to_response('home.html',{'posts': posts,'name' : get_user(request)})


def logout_view(request):
    logout(request)
    return render_to_response('logout.html')



def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reg_success')

    args={}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('success.html')




def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('add_post.html',{ 'form': form },context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render_to_response('blog_post.html',{'post': post,'form': form,},context_instance=RequestContext(request))

