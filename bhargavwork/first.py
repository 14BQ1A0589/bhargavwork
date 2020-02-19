from django.http import HttpResponse
from django.shortcuts import render
import operator


def myf1(request):
    return render(request,"area.html")

def myf2(request):
    return HttpResponse("<h1>Hi Welcome to website</h1>")

def myff(request):
    return render(request,"bhar1.html",{"bb":"1000000000000"})

def aboutus(request):
    return render(request,"aboutus.html")

def count(request):
    cont=request.GET['content']
    wl=cont.split()
    #print(wl)
    wlcount={}
    for word in wl:
        if word in wlcount:
            wlcount[word] += 1
        else:
            wlcount[word]=1
    sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)




    return render(request,"count.html",{"msg":cont,"length":len(wl),"abc":wlcount,'cba':sort1})
