import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from products.models import Product
from products.forms import ProductForm

# Create your views here.
# def product_list(request):
#     return render(
#         request,
#         'products/index.html',
#         {
#             'products': Product.objects.all()
#         }
#     )


class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'
    


# def product_detail(request, pk):
#     return render(
#         request,
#         'products/detail.html',
#         {
#             'product': Product.objects.get(pk=pk)
#         }
#     )


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'


# def product_create(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect(
#                 reverse('products:index')
#             )
#     return render(
#         request,
#         'products/create.html',
#         {
#             'form': form,
#             'page_title': 'Create product'
#         }
        
#     )


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    success_url =  reverse_lazy('products:index')
    form_class = ProductForm


# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
    
#     if request.method == 'POST':
#         product.delete()
#         return redirect(
#             reverse('products:index')
#         )

#     return render(
#         request,
#         'products/delete.html',
#         {
#             'product': product,
#             'page_title': 'Delete product'
#         }
#     )


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm


# def product_update(request, pk):
#     obj = get_object_or_404(Product, pk=pk)
#     form = ProductForm(instance=obj)

#     if request.method == 'POST':
#         form = ProductForm(
#             request.POST, instance=obj
#         )
#     if form.is_valid():
#         form.save()
#         return redirect(
#             reverse('products:index')
#         )
    
#     return render(
#         request,
#         'products/update.html',
#         {
#             'form': form,
#             'page_title': 'Product update'
#         }
#     )


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')
    form_class = ProductForm