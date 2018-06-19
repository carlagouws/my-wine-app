from django import forms
from blog.models import Wine

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('name', 'created_date', 'type', 'variety', 'vintage', 'country', 'comments',)
