from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add-form/', views.add_form, name='add-form'),
    path('update-form/<int:pk>', views.update_form, name='update-form'),
    path('filter-categorical/<int:pk>', views.filter_categorical, name='filter-categorical'),
    path('filter-range/<int:pk>', views.filter_range, name='filter-range'),
]