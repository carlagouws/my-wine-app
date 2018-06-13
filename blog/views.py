from django.shortcuts import render
from blog.models import Wine

def index(request):
    wine = Wine.objects.all().order_by('name')
    return render(request, 'index.html', {'wine': wine,})
