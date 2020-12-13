from django import forms

from app.models import Model2


class Model2Form(forms.ModelForm):
    class Meta:
        model = Model2
        fields = '__all__'


class CategoricalFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        field_name = kwargs.pop('field_name', None)

        super(CategoricalFilterForm, self).__init__(*args, **kwargs)

        self.fields[field_name] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
        self.fields[field_name].choices = choices


class RangeNumberFilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RangeNumberFilterForm, self).__init__(*args, **kwargs)

    from_ = forms.IntegerField()
    to_ = forms.IntegerField()

class RangeDateFilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(RangeDateFilterForm, self).__init__(*args, **kwargs)

    from_ = forms.DateTimeField()
    to_ = forms.DateTimeField()