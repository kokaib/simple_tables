from django.shortcuts import render

from app.models import Model1, Model2, Model3

# Create your views here.

def index(request):
    context = {
        'title': 'Simple Table',
        'table': Model1.table_manager.as_table()
    }
    return render(
        request,
        'with_model_formsets/index.html',
        context
    )