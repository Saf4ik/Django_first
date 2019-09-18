import json
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.urls import reverse, reverse_lazy
from products.models import Category
from products.forms import CategoryForm

# Create your views here.

class CategoryList(ListView):
    model = Category
    template_name = 'categories/index.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    slug_field = 'name'
    context_object_name = 'category'

class CategoryCreate(CreateView):
    model = Category
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:index')
    form_class = CategoryForm


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:index')


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:index')
    form_class = CategoryForm


# def category_content(request, pk):
#     return render(
#         request,
#         'categories/content.html',
#         {
#             'categories': Category.objects.filter(pk=pk)
#         }
#     )


# def category_create(request):
#     form = CategoryForm()
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             # Category.objects.create(
#             #     name=form.cleaned_data.get('name'),
#             #     description=form.cleaned_data.get('description')
#             # )
#             form.save()
#             return redirect(
#                 reverse('products:index')
#             )
#     return render(
#         request,
#         'categories/create.html',
#         {
#             'form': form,
#             'page_title': 'Create category'
#         }
#     )


# def category_delete(request, pk):
#     category = get_object_or_404(Category, pk=pk)
    
#     if request.method == 'POST':
#         category.delete()
#         return redirect(
#             reverse('products:index')
#         )
    
#     return render(
#         request,
#         'categories/delete.html',
#         {
#             'category': category,
#             'page_title': 'Delete category'
#         }
#     )


# def category_update(request, pk):
#     obj = get_object_or_404(Category, pk=pk)
#     form = CategoryForm(instance=obj)

#     if request.method == 'POST':
#         form = CategoryForm(
#             request.POST, instance=obj
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 reverse('products:index')
#             )

#     return render(
#         request,
#         'categories/update.html',
#         {
#             'form': form,
#             'page_title': 'Update category'
#         }
#     )