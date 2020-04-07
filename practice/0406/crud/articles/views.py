from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# Read - All
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# Read - One
def detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

# Create - 폼 보여주기
def new(request):
    return render(request, 'articles/new.html')

# Create - 데이터베이스에 저장하기
def create(request):
    # 저장
    # 1. 저장하려고 하는 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. 실제로 저장하기
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:index')

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')

def edit(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, id):
    # 기존의 데이터
    article = Article.objects.get(id=id)

    # 최신 데이터
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 최신화
    article.title = title
    article.content = content
    article.save()

    # 수정된 게시물로 이동
    # return redirect(f'/articles/{id}/detail')
    return redirect('articles:detail', article.id)