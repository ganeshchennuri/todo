from django.shortcuts import render,redirect, get_object_or_404
from.models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': Task.objects.all(), 'form': form}
    return render(request,'tasks/index.html',context)

def update_task(request, pk):
    task = get_object_or_404(Task,id=pk)
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form':form}
    return render(request,'tasks/update_task.html',context)

def delete_task(request, pk):
    task = get_object_or_404(Task,id=pk)
    
    if request.method=="POST":
        task.delete()
        return redirect('/')
    
    context = {'task': task}
    
    return render(request,'tasks/delete_task.html',context)

def complete_task(request, pk):
    task = get_object_or_404(Task,id=pk)
    task.completed = True
    task.save()
    return redirect('/')