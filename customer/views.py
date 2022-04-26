from django.http import HttpResponse
from django.shortcuts import render


def customer(request):
    context={
        'results': render(request,'item.html'),
        'count': 10,
    }
    return render(request,'customer.html',context)

def cart(request):
    return render(request,'cart.html')