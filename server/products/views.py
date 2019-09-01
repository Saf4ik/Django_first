import json
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category
from .forms import CategoryForm

# Create your views here.
def product_list(request):
    return render(
        request,
        'products/index.html',
        {
            'products': Product.objects.all()
        }
    )


def product_detail(request, pk):
    return render(
        request,
        'products/detail.html',
        {
            'product': Product.objects.get(pk=pk)
        }
    )


def category_create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Category.objects.create(
            #     name=form.cleaned_data.get('name'),
            #     description=form.cleaned_data.get('description')
            # )
            form.save()
            return redirect(
                reverse('products:index')
            )
    return render(
        request,
        'categories/create.html',
        {
            'form': form,
            'page_title': 'Create category'
        }
    )


def category_delete(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(
                name=form.cleaned_data.get('name')
            )
            category.delete()
        return redirect(
            reverse('products:index')
        )
    return render(
        request,
        'categories/delete.html',
        {
            'form': form,
            'page_title': 'Delete category'
        }
    )
