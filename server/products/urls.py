from django.urls import path

from products.views import product_list, product_detail


app_name = 'products'


urlpatterns = [
    path('', product_list, name='index'),
    path('<int:pk>/detail/', product_detail, name='detail')
]