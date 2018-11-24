from django.forms import ModelForm
from django.forms.models import inlineformset_factory


# class ChartCreateForm(forms.ModelForm):
#     class Meta:
#         model = Chart
#         fields = ['name', 'type_chart']


# class ChartUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Chart
#         fields = ['name']


# ChartFormSet = inlineformset_factory(Chart, KPI, form=ChartUpdateForm, extra=1)