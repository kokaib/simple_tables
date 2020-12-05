from django.core.paginator import Paginator
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


def index_paginator(request):
    """
    NOTE: Problem with the paginator: the head row
    """

    context = {
        'title': 'Simple Table',
    }

    table = Model1.table_manager.as_table()
    paginator = Paginator(table, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'add_update_separately/index-paginator.html', context)


def update_form(request, pk):
    context = {}

    instance = Model1.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Model1Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            context['form_status'] = { 'successful': True }
        else:
            context['form_status'] = { 'successful': False }
    else:
        form = Model1Form(instance=instance)
        context['form_status'] = { 'successful': False }

    context['form'] = form

    return render(request, 'add_update_separately/form_fragment.html', context)


def add_form(request):
    context = {}

    if request.method == 'POST':
        form = Model1Form(request.POST)
        if form.is_valid():
            form.save()
            context['form_status'] = { 'successful': True }
        else:
            context['form_status'] = { 'successful': False }
    else:
        form = Model1Form()
        context['form_status'] = { 'successful': False }

    context['form'] = form

    return render(request, 'add_update_separately/form_fragment.html', context)


def filter_categorical(request, pk):
    pass


def filter_range(request, pk):
    pass