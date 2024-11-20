from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burgers

def main(request):
    #return HttpResponse('안녕하세요, 파이버거입니다.')
    return render(request, 'main.html')

def burger_list(request):
    burgers= Burgers.objects.all()
    print('전체 햄버거 목록:', burgers)
    context = { #burgers키에 burgers변수(query set) 전달 
        'burgers' : burgers,
    }
    return render(request, 'burger_list.html', context)

def burger_search(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        burgers = Burgers.objects.filter(name__contains = keyword)
    else:
        burgers = Burgers.objects.none() #빈 쿼리 
        
    context = { #burgers키에 burgers변수(query set) 전달 
        'burgers' : burgers,
    } 
    return render(request, 'burger_search.html',context)

