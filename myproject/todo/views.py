from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import TodoForm



# LIST
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list_todo.html', {'todos': todos})


# CREATE
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Replace with your list view URL name
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form})


# UPDATE
def edit_todo(request, pk):
    # Fetch the To-Do item by primary key (pk)
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()  # Save the updated To-Do
            return redirect('todo_list')  # Redirect to the list view (adjust as needed)
    else:
        form = TodoForm(instance=todo)  # Pre-fill the form with the current To-Do data
    
    return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})



# DELETE 
def delete_todo(request, pk):
    # 1. get_object_or_404 and pass it ModelName & pk
    # item = get_object_or_404(Todo, pk=pk)

    # 2. filter by id
    item = Todo.objects.filter(id=pk).first()
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/home')
