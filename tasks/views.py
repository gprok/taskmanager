from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Task 

# Create your views here.

def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_tasks.html', {'tasks': tasks})


@login_required
def dashboard(request):
    user = request.user
    user_tasks = user.task_set.filter(completed=0)
    print(user_tasks)
    return render(request, 'dashboard.html', {'username': user.username, 
                                              'tasks': user_tasks})
