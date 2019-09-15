from django.urls import path

from products.views import (
    category_create, category_delete, category_update, category_content,
    CategoryCreate, CategoryUpdate, CategoryDelete,
    CategoryList,
)

app_name = 'categories'


urlpatterns = [
    path('', CategoryList.as_view(), name='index'),
    path('<int:pk>/content/', category_content, name='content'),
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
]

