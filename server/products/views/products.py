import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from products.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super(ProductList, self).get_context_data(**kwargs)
    #     paginator = Paginator(context.get('object_list'), 2)
    #     page_number = self.request.GET.get('page')
    #     context['page'] = paginator.get_page(page_number)

    #     return context
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    slug_field = 'name'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    success_url =  reverse_lazy('products:index')
    fields = ['name', 'description', 'category', 'cost', 'image']


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')
    fields = ['name', 'description', 'category', 'cost', 'image']


# Create your views here.
# def product_list(request):
#     return render(
#         request,
#         'products/index.html',
#         {
#             'products': Product.objects.all()
#         }
#     )


# def product_detail(request, pk):
#     return render(
#         request,
#         'products/detail.html',
#         {
#             'product': Product.objects.get(pk=pk)
#         }
#     )


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


