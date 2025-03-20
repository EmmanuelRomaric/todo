from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, "core/index.html", context )


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        task = Task( 
            user=request.user,
            title=title,
            description=description,
            date=date
            )
        task.save()
        return HttpResponseRedirect(reverse("core:index"))
    return render(request, "core/create_task.html")

def update_task(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        task = Task.objects.get(pk=id)
        task.title = title
        task.description = description
        task.date = date
        task.save()
        return HttpResponseRedirect(reverse("core:index"))
    task = Task.objects.get(pk=id)
    context = {'task':task}
    return render(request, "core/update_task.html", context)


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST': 
        task.delete()
        return HttpResponseRedirect(reverse("core:index"))
    context = {'task':task}
    return render(request, "core/delete_task.html", context)



