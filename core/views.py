from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Article, Video
from itertools import chain

# Create your views here.
def index(request):
    return render(request, 'core/pages/index.html')

def articles_videos(request):
    articles = Article.objects.all().order_by('-date')
    videos = Video.objects.all().order_by('-date')

    for article in articles:
        article.content_type = 'article'

    for video in videos:
        video.content_type = 'video'
    
    content = sorted( chain(articles, videos), key=lambda item: item.date, reverse=True )

    return render(request, 'core/pages/articles_videos.html', {'articles': articles, 'videos': videos, 'content': content})

def qa(request):
    return render(request, 'core/pages/qa.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'core/pages/login.html', {
                'error': "მომხმარებელი ან პაროლი არასწორია"
            })
    return render(request, 'core/pages/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'core/pages/signup.html', {
                'error': 'ასეთი მეილი უკვე არსებობს!'
            })


        if password != confirm:
            return render(request, 'core/pages/signup.html', {
                'error': "პაროლები არ ემთხვევა ერთმანეთს"
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'core/pages/signup.html', {
                'error': "სახელი უკვე დაკავებულია"
            })

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('/')
    return render(request, 'core/pages/signup.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def question(request):
    return render(request, 'core/pages/question.html')

def cow_calculator(request):
    return render(request, 'core/pages/cow_evaluation.html')

def soil_analyzer(request):
    return render(request, 'core/pages/ai-analyser.html')