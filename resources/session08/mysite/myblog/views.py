from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib import messages

from myblog.models import Post
from myblog.forms import PostForm


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)


def add_view(request):
    user = request.user
    if not user.is_authenticated:
        raise PermissionDenied
    if request.method == 'POST':
        form = PostForm(request.POST)
        # handle form submission
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'add.html', context)
