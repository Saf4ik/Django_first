from django.shortcuts import render
from django.utils.html import mark_safe
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = get_template('main/index.html')
    context = {
        'description': 'Главная страница Интернет-витрины',
        'page_title': 'Main Page'
    }

    return HttpResponse(template.render(context))
    
def contacts(request):
    return render(
        request,
        'main/contacts.html',
        {
            'page_title': 'Contacts',
            'contacts': ['Contact 1', 'Contact 2', 'Contact 3', 'Contact 4', 'Contact 5']
        }
    )

def about(request):
        return HttpResponse(
            render_to_string(
                'main/about.html',
                {
                    'description': 'Информационная страница Интернет-витрины',
                    'page_title': 'About'
                }
            )
        )