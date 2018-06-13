from django.shortcuts import render

def index(request):
    number = 6
    return render(request, 'index.html', {'number': number,})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')