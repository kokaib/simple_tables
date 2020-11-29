from django.shortcuts import render

from app.models import Model1, Model2, Model3

from .forms import Model1Form

# Create your views here.

def index(request):
    context = {
        'title': 'Simple Table',
        'table': Model1.table_manager.as_table()
    }
    return render(request, 'add_update_separately/index.html', context)

def update_form(request, pk):
    instance = Model1.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Model1Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = Model1Form(instance=instance)

    context = {
        'form': form,
    }

    return render(request, 'add_update_separately/form_fragment.html', context)

def add_form(request):
    if request.method == 'POST':
        form = Model1Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Model1Form()

    context = {
        'form': form,
    }

    return render(request, 'add_update_separately/form_fragment.html', context)