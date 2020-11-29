from django import forms

from app.models import Model1

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = '__all__'