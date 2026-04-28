from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def jinja(request, name):
    return render(request, "hello/jinja.html", {

        "name" : name.capitalize()
        
    })

def random(request):
    return HttpResponse(f"Random sosis")