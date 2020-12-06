from django.urls import path

from . import views

urlpatterns = [
    path('', views.TableView.as_view(), name='index'),
    path('add/', views.add_form, name='add'),
    path('update/<int:pk>', views.update_form, name='update'),
    path('filter-categorical/<str:field_name>', views.filter_categorical, name='filter-categorical'),
    path('filter-range-number/<str:field_name>', views.filter_range_number, name='filter-range-number'),
    path('filter-range-date/<str:field_name>', views.filter_range_date, name='filter-range-date'),
]