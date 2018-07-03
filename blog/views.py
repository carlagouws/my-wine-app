from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from PIL import Image
from blog.models import Wine
from blog.forms import WineForm, WineFilter

def home(request):
    wine = Wine.objects.all().order_by('name')
    return render(request, 'home.html', {'wine': wine,})

def wine_detail(request, pk):
    wine = Wine.objects.get(pk=pk)
    return render(request, 'wine_detail.html', {'wine': wine,})

@login_required
def edit_wine(request, pk):
    wine = Wine.objects.get(pk=pk)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            # auto_rotate_image(wine.image)
            # if wine.image_2:
            #     auto_rotate_image(wine.image_2)
            return redirect('wine_detail', pk=wine.pk)
    else:
        form = WineForm(instance=wine)
    return render(request, 'edit_wine.html', {'wine': wine, 'form': form,})

@login_required
def new_wine(request):
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # if instance.image != 'default.jpg':
            #     auto_rotate_image(instance.image)
            # if instance.image_2:
            #     auto_rotate_image(instance.image_2)
            return redirect('wine_detail', pk=instance.pk)
    else:
        form = WineForm()
    return render(request, 'new_wine.html', {'form': form,})

@login_required
def delete_wine(self, pk):
    wine = Wine.objects.get(pk=pk)
    wine.delete()
    return redirect('home')

def auto_rotate_image(file):
    image = Image.open('static/media/{}'.format(file))
    if hasattr(image, '_getexif'):
        orientation = 0x0112
        exif = image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                image = image.transpose(rotations[orientation])
    image.save('static/media/{}'.format(file))

def search(request):
    wine_list = Wine.objects.all()
    wine_filter = WineFilter(request.GET, queryset=wine_list)
    return render(request, 'wine_search.html', {'filter': wine_filter})


















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


# def rotate_image(self, im, pk):
#     wine = Wine.objects.get(pk=pk)
#     image = Image.open('static/media/{}'.format(im))
#     if hasattr(image, '_getexif'):
#         orientation = 0x0112
#         exif = image._getexif()
#         if exif is not None:
#             orientation = exif[orientation]
#             rotations = {
#                 3: Image.ROTATE_180,
#                 6: Image.ROTATE_270,
#                 8: Image.ROTATE_90
#             }
#             if orientation in rotations:
#                 image = image.transpose(rotations[orientation])
#     image.save('static/media/{}'.format(im))
#     return redirect('wine_detail', pk=wine.pk)
