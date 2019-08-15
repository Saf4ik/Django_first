import json
from django.shortcuts import render

# Create your views here.
def product_list(request):
    with open('products/fixtures/data.json') as file:
        return render(
            request, 
            'products/index.html',
            {
                'page_title': 'Catalog',
                'products': json.load(file)
            }
        )

def product_detail(request, pk):
    with open('products/fixtures/data.json') as file:
        return render(
            request,
            'products/detail.html',
            {
                'product': json.load(file)[pk],
                'page_title': 'Detail'
            }
            
        )