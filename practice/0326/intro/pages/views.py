from django.shortcuts import render

# Create your views here.
def lotto(request):
    import random

    numbers = range(1,46)
    lucky = random.sample(numbers,6)

    context = {
        'lotto' : lucky,
        'name' : 'Jeon',
        'today' : '20200326'
    }

    return render(request,'lotto.html',context)

def iam(request):
    context = {
        'myname' : '전석현'
    }

    return render(request,'iam.html',context)

def lunch(request):
    menupan = ['빅맥','더콰트로치즈와퍼','페페로니피자','장어','초밥','힌우','삼겹살']
    context = {
        'menu' : menupan
    }

    return render(request, 'lunch.html', context)


def hi(request, name):
    context = {
        'name': name
    }
    return render(request, 'hi.html',context)



def dinner(request, menu, num):
    context = {
        'menu': menu,
        'num': num
    }

    return render(request, 'dinner.html', context)