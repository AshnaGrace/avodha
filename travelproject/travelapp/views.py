from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
# def fun(request):
#     return render(request,"home.html",
#                   {'name':'addition'})

from .models import news, place


def fun(request):
    obj=place.objects.all()
    # obj=place()
    # obj.name="kerala"
    # obj.price=100
    # obj.desc="this is kerala"
    return render(request,"index.html",{'results':obj})
def test(request):
    ash=news.objects.all()
    return render(request,"index.html",{'tests':ash})

def addition(request):
    num1var=int(request.POST["num1"])
    num2var=int(request.POST["num2"])
    num3=num1var+num2var
    return render(request,"result.html",{"add":num3})
