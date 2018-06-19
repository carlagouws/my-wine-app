from django.shortcuts import render, redirect
from blog.models import Wine
from blog.forms import WineForm

def home(request):
    wine = Wine.objects.all().order_by('name')
    return render(request, 'home.html', {'wine': wine,})

def wine_detail(request, pk):
    wine = Wine.objects.get(pk=pk)
    return render(request, 'wine_detail.html', {'wine': wine,})

def edit_wine(request, pk):
    wine = Wine.objects.get(pk=pk)
    if request.method == 'POST':
        form = WineForm(data=request.POST, instance=wine)
        if form.is_valid():
            form.save()
            return redirect('wine_detail', pk=wine.pk)
    else:
        form = WineForm(instance=wine)
    return render(request, 'edit_wine.html', {'wine': wine, 'form': form,})

def new_wine(request):
    if request.method == 'POST':
        form = WineForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WineForm()
    return render(request, 'new_wine.html', {'form': form,})

















# # GET request to get a blank form to create a new instance
# form = MyModelForm()
#
# # POST request to save a new instance
# form = MyModelForm(request.POST)
# form.save()
#
# # GET request to get a form prefilled with values from an existing model instance
# form = MyModelForm(instance=my_model_instance)
#
# # POST request to save changes to an existing model instance
# form = MyModelForm(request.POST, instance=my_model_instance)
# form.save()