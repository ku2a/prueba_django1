from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Project,Task
from .forms import CreateNewTask
def hello(request,usuario=""):
    print(usuario,"#########")
    if usuario !="" and usuario!="admin":
        nico = Project.objects.get(name=usuario)
        task = Task.objects.filter(project=nico)
        
    else: nico = "CACA"
    return render(request,'index.html',{'titulo':nico, 'tasks':task})

def index(request):
    return HttpResponse("AAAAAAAAAAAAAAAAAAAA")


def create_task(request:HttpRequest):
    
    
    if request.method == "GET":
        pass
        
    elif request.method == "POST":
        print(request.POST)
        Task.objects.create(title = request.POST["title"],description = request.POST["description"],project_id=3)
        return redirect("/create_task")
    return render(request, 'create_task.html', {'form': CreateNewTask()})