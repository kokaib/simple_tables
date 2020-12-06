import datetime

from django.views import generic
from django.shortcuts import render

from app.models import Model2, Model2, Model3

from .forms import Model2Form

# Create your views here.


def index(request):
    context = {}
    context['title'] = 'Simple Table'
    return render(request, 'class_based_view_without_custom_manager/index.html', context)


class TableView(generic.ListView):
    model = Model2
    paginate_by = 3
    context_object_name = 'table_rows'
    template_name = 'class_based_view_without_custom_manager/index.html'

    def get_queryset(self):
        filter_expr = {}
        # TODO: 1) eliminate double iteration
        #       2) DRY with options
        for field_name in [x['name'] for x in self.model.get_table_columns() if 'filterable' in self.model.get_column_options(x['name'])]:
            options = self.model.get_column_options(field_name)
            if 'categorical' in options:
                filtered_values = self.request.GET.getlist(field_name)
                if filtered_values:
                    filter_expr[f'{field_name}__in'] = filtered_values
            elif 'range' in options:
                filter_from = self.request.GET.get(f'{field_name}_from')
                filter_to = self.request.GET.get(f'{field_name}_to')
                if filter_from and filter_to:
                    filter_expr[f'{field_name}__range'] = (filter_from, filter_to)

        queryset = self.model.objects.filter(**filter_expr)
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
    return render(request, 'class_based_view_without_custom_manager/categorical_filter_form_fragment.html', context)


def filter_range_number(request, field_name):
    context = {}
    context['form_fields'] = {
        'from': {
            'id': f'{field_name}_from',
            'name': f'{field_name}_from',
            'label': 'From:',
            'default': 0,
        },
        'to': {
            'id': f'{field_name}_to',
            'name': f'{field_name}_to',
            'label': 'To:',
            'default': 100,
        }
    }
    return render(request, 'class_based_view_without_custom_manager/range_number_filter_form_fragment.html', context)


def filter_range_date(request, field_name):
    context = {}
    context['form_fields'] = {
        'from': {
            'id': f'{field_name}_from',
            'name': f'{field_name}_from',
            'label': 'From:',
            'default': datetime.datetime(1900, 1, 1),
        },
        'to': {
            'id': f'{field_name}_to',
            'name': f'{field_name}_to',
            'label': 'To:',
            'default': datetime.datetime.now(),
        }
    }
    return render(request, 'class_based_view_without_custom_manager/range_date_filter_form_fragment.html', context)