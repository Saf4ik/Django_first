from django.urls import path

from products.views import (
    # product_list, product_detail, 
    ProductCreate, ProductDelete, 
    ProductUpdate, ProductList, ProductDetail
    # product_create, product_update, product_delete
)


app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    # path('', product_list, name='index'),
    path('<slug:slug>/detail/', ProductDetail.as_view(), name='detail'),
    # path('<int:pk>/detail/', product_detail, name='detail'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
    # path('<int:pk>/delete/', product_delete, name='delete'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    # path('<int:pk>/update/', product_update, name='update'),
]