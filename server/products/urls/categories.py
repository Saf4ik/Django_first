from django.urls import path

from products.views import (
    CategoryCreate, CategoryUpdate, CategoryDelete, CategoryList, CategoryDetail
)

app_name = 'categories'


urlpatterns = [
    path('', CategoryList.as_view(), name='index'),
    path('<slug:slug>/detail/', CategoryDetail.as_view(), name='detail'),
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
]

