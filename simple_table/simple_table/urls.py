"""simple_table URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='table/', permanent=True)),
    path('table/', include('app.urls')),
    path('table-add-update-separately/', include('add_update_separately.urls')),
    path('table-with-model-formsets/', include('with_model_formsets.urls')),
    path('class-based-view-without-custom-manager/', include('class_based_view_without_custom_manager.urls')),
    path('without-ajax/', include('without_ajax.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)