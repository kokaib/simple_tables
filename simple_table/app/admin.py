from django.contrib import admin

from .models import Model1, Model2, Model3

# Register your models here.

@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    pass

@admin.register(Model2)
class Model2Admin(admin.ModelAdmin):
    pass

@admin.register(Model3)
class Model3Admin(admin.ModelAdmin):
    pass