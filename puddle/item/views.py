from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . models import Category, Item
from . forms import ItemForm, ItemUpdateForm


def item(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categorys = Category.objects.all()
    items = Item.objects.filter(is_solded=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = Item.objects.filter(name__icontains=query)

    return render(request, 'item/item.html', {
        'category_id': int(category_id),
        'categorys': categorys,
        'items': items,
        'query': query
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@staff_member_required
def update_new_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemUpdateForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = ItemUpdateForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })


@staff_member_required
def new(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = ItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    # return redirect('dashboard:inbox')