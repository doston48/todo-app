from django.shortcuts import render 
from django.http import HttpResponse
from .models import todo

def todo_list(request):
    todos = todo.objects.alL()

    
# models.py U

   
    return render(request, 'todoapp/base.html')
    


def pending_todos(request):
    todos = todo.objects.filter(is_completed=False)
    response = ""
        
    for todo in todos:
        response += f"{todo.title}\n{todo.priority}\n{todo.due_date}\n"
 

def completed_todos(request):
     pass