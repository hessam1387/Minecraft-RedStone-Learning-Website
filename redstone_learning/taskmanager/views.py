from django.shortcuts import render

# Create your views here.
tasks = ['abbas', 'mmd', 'akbar']

def index(request):

    return render(request, 'taskmanager/index.html', {
        "tasks" : tasks
    })


def add(request):

    return render(request, 'taskmanager/add.html', {
        
})