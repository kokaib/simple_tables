from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.TableView.as_view(), name='table'),
    #
    path('add/', views.add_form, name='add'),
    path('update/<int:pk>', views.update_form, name='update'),
    #
    path('filter-categorical-entrypoint/<str:model_name>/<str:field_name>', views.filter_categorical_entrypoint, name='filter-categorical-entrypoint'),
    path('filter-categorical/<str:model_name>/<str:field_name>', views.filter_categorical, name='filter-categorical-a'),
    #
    path('filter-range-number-entrypoint/<str:model_name>/<str:field_name>', views.filter_range_number_entrypoint, name='filter-range-number-entrypoint'),
    path('filter-range-number/<str:model_name>/<str:field_name>', views.filter_range_number, name='filter-range-number-a'),
    #
    path('filter-range-date-entrypoint/<str:model_name>/<str:field_name>', views.filter_range_date_entrypoint, name='filter-range-date-entrypoint'),
    path('filter-range-date/<str:model_name>/<str:field_name>', views.filter_range_date, name='filter-range-date-a'),
]