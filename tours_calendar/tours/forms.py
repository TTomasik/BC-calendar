from django import forms
from tours.models import Tour
from django.forms import ModelForm


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'
        exclude = ['date_of_entry', ]



