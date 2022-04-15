from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


# Create your views here.
def products(request):
    return render(request, 'mainapp/products.html')


# Create your views here.
def contact(request):
    return render(request, 'mainapp/contact.html')
