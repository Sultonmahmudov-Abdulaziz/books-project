from django.contrib import admin
from .models import Books,Language,BooksAutor,Author,Comment


admin.site.register(Books)

admin.site.register(Language)

admin.site.register(BooksAutor)

admin.site.register(Author)

admin.site.register(Comment)
