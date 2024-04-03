from django.shortcuts import render

from apps.models import Contact


def index_views(request):
    context = {
        'contact': Contact.objects.all()
    }
    return render(request, 'apps/index.html', context)


def item_list(request):
    items = Contact.objects.all()
    context = {
        'items': items
    }
    return render(request, 'apps/list.html', context)
