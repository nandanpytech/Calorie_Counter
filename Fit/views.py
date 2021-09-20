from Fit.models import Contact
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Fit.models import Contact,Product
from math import ceil
from django.conf import settings

# Create your views here.
def home(request):
    allProds=[]
    prod=Product.objects.all()
    print(prod)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(1, nSlides), nSlides])
    return render(request,'home.html',{'allProds':allProds})
def about(request):
    return render (request,'about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        adress=request.POST.get('adress')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,adress=adress,desc=desc)
        contact.save()
    return render (request,'contact.html')

