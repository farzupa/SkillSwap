from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, "index.html")
    #return HttpResponse("Hello, world! This is the home page.")


def learnskill(request):
    return render(request, "learnskill.html")



def teachskill(request):
    return render(request, "teachskill.html")

def makegroup(request):
    return render(request, "makegroup.html")


# Create your views here.
