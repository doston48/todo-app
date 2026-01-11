from django.shortcuts import render 
from django.http import HttpResponse
from .models import todo

def todo_list(request):
    todos = todo.objects.all()
    response =  ""
    
# models.py U

    for todo in todos:
          status = "Done" if todo.is_completed else "Not Done"
          response += f"{todo.title} - {status}"
    
    
    return HttpResponse(response)

def pending_todos(request):
    todos = todo.objects.filter(is_completed=False)
    response = ""
        
    for todo in todos:
        response += f"{todo.title}"\n{todo.priority}\n{todo.due_date}\n
 

def completed_todos(request):
     pass