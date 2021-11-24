from django.shortcuts import render

# Create your views here.


def homeview(request):
    template_name='firstapp/home.html'
    context = {}
    return render(request, template_name, context)


def aboutusview(request):
    template_name = 'firstapp/aboutus.html'
    context = {}
    return render(request, template_name, context)