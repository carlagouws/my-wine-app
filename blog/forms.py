from django import forms
from blog.models import Wine

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('name', 'created_date', 'image', 'image_2', 'type', 'variety', 'vintage', 'region', 'comments',)
