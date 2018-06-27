from django import forms
from blog.models import Wine
import django_filters

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('name', 'created_date', 'image', 'image_2', 'rating', 'type', 'variety', 'vintage', 'region', 'shop', 'price', 'comments',)

class WineFilter(django_filters.FilterSet):
    class Meta:
        model = Wine
        fields = ['type', 'shop', 'rating', ]
