import datetime

from django.db.models import Max, Min
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.http import HttpResponseBadRequest

from django.views import generic
from django.shortcuts import render

from app.models import Model2, Model2, Model3

from .forms import Model2Form, CategoricalFilterForm, RangeNumberFilterForm, RangeDateFilterForm

# NOTE: passing rendered html in json is unlikely to be a good practice


def index(request):
    context = {}
    context['title'] = 'Simple Table'

    return render(request, 'class_based_view_without_custom_manager/index.html', context)


class TableView(generic.ListView):
    model = Model2
    paginate_by = 3
    context_object_name = 'table_rows'
    template_name = 'class_based_view_without_custom_manager/table.html'

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
    
    def get(self, *args, **kwargs):
        t = super().get(*args, **kwargs)
        t.render()

        return JsonResponse(
            {
                'id': 'table',
                'data': {
                    'request_get': self.request.GET.urlencode(),
                    'is_successful': True,
                    'response_text': t.content.decode('utf-8'),
                },
            }
        )


def update_form(request, pk):
    context = {}

    instance = Model2.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Model2Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return TableView.as_view()(request)
    else:
        form = Model2Form(instance=instance)
    
    context['form'] = form

    t = TemplateResponse(request, 'class_based_view_without_custom_manager/form_fragment.html', context)
    t.render()

    return JsonResponse(
        {
            'id': 'table',
            'data': {
                'request_get': request.GET.urlencode(),
                'is_successful': False,
                'response_text': t.content.decode('utf-8'),
            },
        }
    )


def add_form(request):
    context = {}

    if request.method == 'POST':
        form = Model2Form(request.POST)
        if form.is_valid():
            form.save()
            return TableView.as_view()(request)
    else:
        form = Model2Form()

    context['form'] = form

    t = TemplateResponse(request, 'class_based_view_without_custom_manager/form_fragment.html', context)
    t.render()

    return JsonResponse(
        {
            'id': 'table',
            'data': {
                'request_get': request.GET.urlencode(),
                'is_successful': False,
                'response_text': t.content.decode('utf-8'),
            },
        }
    )


def get_model(model_name):
    if model_name == 'Model2':
        return Model2


def filter_categorical(request, model_name, field_name):
    if request.method == 'GET':
        
        context = {}

        model = get_model(model_name)

        # list of tuples: [(label1, value1), (label2, value2), ... ]
        choices = [(v, v) for v in model.objects.order_by().values_list(field_name, flat=True).distinct()]

        if request.GET:
            form = CategoricalFilterForm(request.GET, field_name=field_name, choices=choices)
            if form.is_valid():
                return TableView.as_view()(request)
        else:
            form = CategoricalFilterForm(field_name=field_name, choices=choices)

        context['form'] = form

        t = TemplateResponse(request, 'class_based_view_without_custom_manager/categorical-filter-form-fragment.html', context)
        t.render()

        return JsonResponse(
            {
                'id': 'table',
                'data': {
                    'request_get': request.GET.urlencode(),
                    'is_successful': False,
                    'response_text': t.content.decode('utf-8'),
                }
            }
        )
    
    return HttpResponseBadRequest()


def filter_range_number(request, model_name, field_name):
    if request.method == 'GET':
        context = {}

        model = get_model(model_name)

        default_from = model.objects.aggregate(Min(field_name))[f'{field_name}__min']
        default_to = model.objects.aggregate(Max(field_name))[f'{field_name}__max']
        
        if request.GET and request.GET.get('from_') and request.GET.get('to_'):
            form = RangeNumberFilterForm(initial={'from_': request.GET.get('from_'), 'to_': request.GET.get('to_')})
            if form.is_valid():
                return TableView.as_view()(request)
        else:
            form = RangeNumberFilterForm(initial={'from_': default_from, 'to_': default_to})

        context['form'] = form

        t = TemplateResponse(request, 'class_based_view_without_custom_manager/range-number-filter-form-fragment.html', context)
        t.render()

        return JsonResponse(
            {
                'id': 'table',
                'data': {
                    'request_get': request.GET.urlencode(),
                    'is_successful': False,
                    'response_text': t.content.decode('utf-8'),
                }
            }
        )
    
    return HttpResponseBadRequest()


def filter_range_date(request, model_name, field_name):
    if request.method == 'GET':
        context = {}

        model = get_model(model_name)

        default_from = model.objects.aggregate(Min(field_name))[f'{field_name}__min']
        default_to = model.objects.aggregate(Max(field_name))[f'{field_name}__max']
        
        if request.GET and request.GET.get('from_') and request.GET.get('to_'):
            form = RangeDateFilterForm(initial={'from_': request.GET.get('from_'), 'to_': request.GET.get('to_')})
            if form.is_valid():
                return TableView.as_view()(request)
        else:
            form = RangeDateFilterForm(initial={'from_': default_from, 'to_': default_to})
            context['form_status'] = { 'successful': False }

        context['form'] = form

        t = TemplateResponse(request, 'class_based_view_without_custom_manager/range-date-filter-form-fragment.html', context)
        t.render()

        return JsonResponse(
            {
                'id': 'table',
                'data': {
                    'request_get': request.GET.urlencode(),
                    'is_successful': False,
                    'response_text': t.content.decode('utf-8'),
                }
            }
        )
    
    return HttpResponseBadRequest()