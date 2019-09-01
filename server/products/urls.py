from django.urls import path

from .views import (
    product_list, product_detail, category_create, category_delete
)


app_name = 'products'


urlpatterns = [
    path('', product_list, name='index'),
    path('<int:pk>/detail/', product_detail, name='detail'),
    path('create/', category_create, name='create'),
    path('delete/', category_delete, name='delete')
]