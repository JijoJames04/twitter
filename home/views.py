from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from textblob import TextBlob

from home.models import Post


@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', context={"posts": posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        image = request.FILES.get('image')

        if not content:
            return redirect('home', permanent=True)

        blob = TextBlob(content)
        Post.objects.create(content=content, author=request.user, image=image, sentiment=blob.sentiment.polarity)

    return redirect('home', permanent=True)
