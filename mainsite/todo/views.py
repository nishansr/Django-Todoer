from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Todo
from .forms import TodoForm

# ! Homepage
def home(request):
    todos = Todo.objects.all()
    form = TodoForm()    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'base.html', context)

# ! Updating
def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
        context = {
            'form': form
        }
    return render(request, 'update.html', context)

# ! Removing
def delete(request, pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect("/")

# ! Completing
def finish(request, pk):
    todo = Todo.objects.get(id = pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('/')

# ! Searching
def search(request):
    query = request.GET['query']
    todos = Todo.objects.filter(title__icontains = query)
    context = {
        'todos': todos
    }
    return render(request, 'search.html', context)

# ! Detailing
def details(request, pk):
    todos= Todo.objects.get(id=pk)
    context = {
        'todos': todos
    }
    return render(request, 'details.html', context)