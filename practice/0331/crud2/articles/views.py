from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    # db에서 전체 글 목록 가져오기
    articles = Article.objects.all()

    context = {
        'articles':articles
    }
    return render(request, 'index.html',context)


def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return render(request, 'create.html')
    
   