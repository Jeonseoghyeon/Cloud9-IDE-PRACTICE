from django.shortcuts import render
import requests
from pprint import pprint

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    # 사용자가 입력한 키워드 가져오기
    keyword = request.GET.get('search')
    # 키워드로 사진 가져오기
    url = f'https://api.unsplash.com/search/photos/?client_id=5ELz6iy1jjyAqO3ok3x1f-Gzk5HHZb_5KgstWzvclm0&query={keyword}'
    res = requests.get(url).json()
    # 가져온 사진 보여주기
    # pprint(res)
    image_list = res.get('results')
    result = []
    for image in image_list:
        i = image.get('urls').get('regular')
        result.append(i)

    print(result)
    context = {
        'result' : result
    }
    return render(request,'gallery.html',context)