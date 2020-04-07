from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)



def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)


#게시물 생성 기능

def create(request):
    # 1-4. 사용자가 데이터를 입력해서 저장 요청을 보낸다.(POST)
    # 1-10. 사용자가 올바른 데이터를 입력해서 저장 요청을 보낸다.
    if request.method == 'POST':
        # 1-5. 입력한 데이터를 폼에 담는다.
        # 1-11. 입력한 데이터를 폼에 담는다.
        form = ArticleForm(request.POST)
        # 1-6. 유효성 검사를 한다.
        # 1-12. 유효성 검사를 한다.
        if form.is_valid():
            # 1-13. 유효성 검사를 통과하고 저장한다.
            article = form.save()
            # 1-14. 작성된 글로 넘겨준다.
            return redirect('articles:detail', article.id)


    # 1-1. 사용자에게 폼을 보여준다.(GET)
    else:
        # 1-2. 폼을 생성한다.
        form = ArticleForm()
    context={
        'form':form
    }
    # 1-3. 폼을 사용자에게 보내준다.
    return render(request,'articles/create.html',context)

    # # 1-7. (유효성 검사 실패한 경우)
    # # 1-8. 새로운 Form을 다시 만든다.
    # form = ArticleForm()
    # context = {
    #     'form':form
    # }
    # # 1-9. 새로운 Form을 보내준다.
    # return render(request, 'articles/create.html',context)

def update(request,pk):
    # article = get_object_or_404(pk=pk)
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form':form
    }
    return render(request, 'articles/update.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
