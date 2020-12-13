import datetime

from .utils import qs2dict, dict2qs, merge_qss, get_model

from django.db.models import Max, Min
from django.http import HttpResponseBadRequest

from django.views import generic
from django.urls import reverse
from django.shortcuts import render, redirect

from app.models import Model2

from .forms import Model2Form, CategoricalFilterForm, RangeNumberFilterForm, RangeDateFilterForm


class TableView(generic.ListView):
    model = Model2
    paginate_by = 3
    context_object_name = 'table_rows'
    template_name = 'without_ajax/index.html'

    def get_queryset(self):
        print(f'table view: {self.request.GET}')

        filter_expr = {}

        # TODO: 1) DRY with options
        
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


def add_form(request):
    context = {}

    if request.method == 'POST':
        form = Model2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = Model2Form()

    context['form'] = form
    context['title'] = 'Add'

    return render(request, 'without_ajax/form-fragment.html', context)


def update_form(request, pk):
    context = {}

    instance = Model2.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Model2Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = Model2Form(instance=instance)
    
    context['form'] = form
    context['title'] = 'Update'

    return render(request, 'without_ajax/form-fragment.html', context)


def filter_categorical(request, model_name, field_name):
    if request.method == 'GET':
        context = {}

        state = request.GET.get('state')
        qs = request.GET.urlencode()

        print(f'state: {state}')
        print(f'qs: {qs}')

        model = get_model(model_name)

        # list of tuples: [(label1, value1), (label2, value2), ... ]
        choices = [(v, v) for v in model.objects.order_by().values_list(field_name, flat=True).distinct()]

        if request.GET:
            form = CategoricalFilterForm(request.GET, field_name=field_name, choices=choices)
            if form.is_valid():
                redirect_to_qs = merge_qss(state, qs) if state else qs
                
                print(f'redirect to qs: {redirect_to_qs}')

                redirect_to = f"{reverse('table')}?{redirect_to_qs}"
                return redirect(redirect_to)
        else:
            form = CategoricalFilterForm(field_name=field_name, choices=choices)

        context['form'] = form
        context['title'] = 'Filter'
        context['action'] = reverse('filter-categorical', args=(model_name, field_name))
        context['state'] = state

        return render(request, 'without_ajax/categorical-filter-form-fragment.html', context)
    
    return HttpResponseBadRequest()


def filter_range_number(request, model_name, field_name):
    if request.method == 'GET':
        context = {}

        state = request.GET.get('state')
        qs_raw = request.GET.urlencode()

        print(f'state: {state}')
        print(f'qs: {qs_raw}')

        model = get_model(model_name)
        
        if request.GET and request.GET.get('from_') and request.GET.get('to_'):
            form = RangeNumberFilterForm(request.GET)
            if form.is_valid():
                qs_raw_dict = qs2dict(qs_raw)
                d = {
                    f'{field_name}_from': qs_raw_dict['from_'],
                    f'{field_name}_to': qs_raw_dict['to_'],
                }
                qs = dict2qs(d)

                redirect_to_qs = merge_qss(state, qs) if state else qs
                
                print(f'redirect to qs: {redirect_to_qs}')

                redirect_to = f"{reverse('table')}?{redirect_to_qs}"
                return redirect(redirect_to)
        else:
            default_from = model.objects.aggregate(Min(field_name))[f'{field_name}__min']
            default_to = model.objects.aggregate(Max(field_name))[f'{field_name}__max']

            form = RangeNumberFilterForm(initial={'from_': default_from, 'to_': default_to})

        context['form'] = form
        context['title'] = 'Filter'
        context['action'] = reverse('filter-range-number', args=(model_name, field_name))
        context['state'] = state

        return render(request, 'without_ajax/range-filter-form-fragment.html', context)
    
    return HttpResponseBadRequest()


def filter_range_date(request, model_name, field_name):
    if request.method == 'GET':
        context = {}

        state = request.GET.get('state')
        qs_raw = request.GET.urlencode()

        print(f'state: {state}')
        print(f'qs: {qs_raw}')

        model = get_model(model_name)
        
        if request.GET and request.GET.get('from_') and request.GET.get('to_'):
            form = RangeDateFilterForm(request.GET)
            if form.is_valid():
                qs_raw_dict = qs2dict(qs_raw)
                d = {
                    f'{field_name}_from': qs_raw_dict['from_'],
                    f'{field_name}_to': qs_raw_dict['to_'],
                }
                qs = dict2qs(d)

                redirect_to_qs = merge_qss(state, qs) if state else qs
                
                print(f'redirect to qs: {redirect_to_qs}')

                redirect_to = f"{reverse('table')}?{redirect_to_qs}"
                return redirect(redirect_to)
        else:
            default_from = model.objects.aggregate(Min(field_name))[f'{field_name}__min']
            default_to = model.objects.aggregate(Max(field_name))[f'{field_name}__max']

            form = RangeDateFilterForm(initial={'from_': default_from, 'to_': default_to})

        context['form'] = form
        context['title'] = 'Filter'
        context['action'] = reverse('filter-range-date', args=(model_name, field_name))
        context['state'] = state

        return render(request, 'without_ajax/range-filter-form-fragment.html', context)
    
    return HttpResponseBadRequest()