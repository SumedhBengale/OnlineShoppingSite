from django.http import HttpResponse
from django.shortcuts import render
from django import template
register = template.Library()

@register.inclusion_tag('item.html')
def manager(request):
    context={
        'results': render(request,'item.html'),
        'count': 5,
        
    }
    return render(request, 'manager.html',context)