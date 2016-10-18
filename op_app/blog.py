from django.shortcuts import render_to_response
from op_app import models


def index(request):
    blog_list = models.Blog.objects.all()
    return render_to_response('blog/index.html', {'blog_list': blog_list})
