from django.views import generic
from django.shortcuts import render

from app.models import Model2, Model2, Model3

from .forms import Model2Form

# Create your views here.


class TableView(generic.ListView):
    model = Model2
    paginate_by = 3
    context_object_name = 'table_rows'
    template_name = 'class_based_view_without_custom_manager/index.html'

    def get_queryset(self):
        filter_expr = {}
        for field_name in [x['name'] for x in self.model.get_table_columns()]:
            filtered_values = self.request.GET.getlist(field_name)
            print(filtered_values)
            if filtered_values:
                filter_expr[f'{field_name}__in'] = filtered_values
        print(filter_expr)
        queryset = self.model.objects.filter(**filter_expr)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Simple Table'
        context['table_columns'] = self.model.get_table_columns()
        return context


def update_form(request, pk):
    context = {}

    instance = Model2.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Model2Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            context['form_status'] = { 'successful': True }
        else:
            context['form_status'] = { 'successful': False }
    else:
        form = Model2Form(instance=instance)
        context['form_status'] = { 'successful': False }
    
    context['form'] = form

    return render(request, 'class_based_view_without_custom_manager/form_fragment.html', context)


def add_form(request):
    context = {}

    if request.method == 'POST':
        form = Model2Form(request.POST)
        if form.is_valid():
            form.save()
            context['form_status'] = { 'successful': True }
        else:
            context['form_status'] = { 'successful': False }
    else:
        form = Model2Form()
        context['form_status'] = { 'successful': False }

    context['form'] = form

    return render(request, 'class_based_view_without_custom_manager/form_fragment.html', context)


def filter_categorical(request, field_name):
    context = {}
    context['filter'] = {
        'name': field_name,
        'vals': Model2.objects.order_by().values_list(field_name, flat=True).distinct(),
    }
    return render(request, 'class_based_view_without_custom_manager/filter_form_fragment.html', context)


def filter_range(request, field_name):
    pass