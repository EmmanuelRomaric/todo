from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def mysignup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            login(request, user)
            return HttpResponseRedirect(reverse("core:index"))
    return render(request, 'core/signup.html',)


def index(request):
    tasks = Task.objects.filter(user=request.user)
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



