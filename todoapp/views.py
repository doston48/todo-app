
from django.http import HttpResponse
from django.shortcuts import render 
from .models import todo



def todo_list(request):
    todos = todo.objects.all()

    
# models.py U

   
    return render(request, 'todoapp/base.html', {})
    


def pending_todos(request):
    todos = todo.objects.filter(is_completed=False)
    response = ""
        
    for todo in todos:
        response += f"{todo.title}\n{todo.priority}\n{todo.due_date}\n"
 
    return HttpResponse(response)

def completed_todos(request):
    todos = todo.objects.filter(is_completed = True)
    reponse = ""
     
    for todo in todos:
        

    response += f"{todo.title}\n"