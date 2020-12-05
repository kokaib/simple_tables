from django import forms

from app.models import Model2

class Model2Form(forms.ModelForm):
    class Meta:
        model = Model2
        fields = '__all__'