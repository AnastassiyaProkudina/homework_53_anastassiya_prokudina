from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from to_do_list.models import Task

def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date_to_do': request.POST.get('date_to_do'),
    }
    task = Task.objects.create(**task_data)
    return redirect(reverse('task_detail', kwargs={'pk':task.pk}))

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={"task": task})

def delete_view(request, pk, ):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')


