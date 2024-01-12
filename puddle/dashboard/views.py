from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from item.models import Item, Category

@staff_member_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items
    })