from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    context = {'phones': Phone.objects.values().order_by('name')}
    if sort_param == 'name':
        context = {'phones': Phone.objects.values().order_by('name')}
    elif sort_param == 'min_price':
        context = {'phones': Phone.objects.values().order_by('price')}
    elif sort_param == 'max_price':
        context = {'phones': Phone.objects.values().order_by('-price')}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug)[0]}
    return render(request, template, context)
