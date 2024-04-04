from django.shortcuts import render
from users.models import Books

def landing_page(request):
    books = Books.objects.all().order_by("name")

    data = {
        "books":books,
    }
    return render(request, template_name='landing.html', context=data)