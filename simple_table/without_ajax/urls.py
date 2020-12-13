from django.urls import path

from . import views

urlpatterns = [
    path('', views.TableView.as_view(), name='table'),
    path('add/', views.add_form, name='add'),
    path('update/<int:pk>', views.update_form, name='update'),
    path('filter-categorical/<str:model_name>/<str:field_name>', views.filter_categorical, name='filter-categorical'),
    path('filter-range-number/<str:model_name>/<str:field_name>', views.filter_range_number, name='filter-range-number'),
    path('filter-range-date/<str:model_name>/<str:field_name>', views.filter_range_date, name='filter-range-date'),
]