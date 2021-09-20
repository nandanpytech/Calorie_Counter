from django.shortcuts import render
from django.http import HttpResponse
from Cut.models import Search_List
from math import ceil
# Create your views here.
def index(request):
    return HttpResponse('hii')
def search_list(request):
    allProds=[]
    prod=Search_List.objects.all()
    print(prod)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(1, nSlides), nSlides])
    return render(request,'search_list.html',{'allProds':allProds} )

def productView(request,myid):
    product=Search_List.objects.filter(id=myid)          #it is just fetch the product_name directly
    return render(request, "prodView.html",{"product":product[0]})

def search(request):
    query=request.GET['search']
    if len(query)>20:
        allPost=Search_List.objects.none
    else:    
        listname=Search_List.objects.filter(list_name__icontains=query)
        allPost=listname
    params={'allPost':allPost,'query':query}
    return render (request,'search.html',params)

def consumed(request):
    return render(request,'consumed.html')