
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .forms import todoform

from .models import todo



def todo_list(request):
    todos = todo.objects.all()
    
    return render(request, 'todoapp/todo_list.html', {'todos': todos})

   
def pending_todos(request):
    todos = todo.objects.filter(is_completed=False)
    response = ""
    
    for todo in todos:
     response += f"{todo.title}\n{todo.priority}\n{todo.due_date}\n"
    
    return HttpResponse(response)

def completed_todos(request):
    todos = todo.objects.filter(is_completed = True)
    response = ""


   
    
    


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
    
def add_todo(request):
    if request.method == 'POST':
        form = todoform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    else:
        form = todoform()
            
    return render(request, 'todoapp/todo_form.html',{'form': form})
        
def update_todo(request, pk):
    todo = get_object_or_404(todo, pk=pk)
    
    if request method == 'POST':
       form = todoform(request.POST, instance=todo)
       is form.is_valid():
           from.save()
           return redirect('todo_list')
    else:
        form = todoform(instance=todo)
        return render(request)
            
            