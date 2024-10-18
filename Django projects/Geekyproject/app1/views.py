from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello_Gautam(request):
    return HttpResponse(50+60)

def Hello_render(request):
    coursename={'cname':'React'}
    return render(request,'index.html',context=coursename)


def Main_render(request):
    return render(request,'app1/newcourse.html')
