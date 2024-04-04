from django.contrib import admin
from .models import Books,Language,BooksAutor,Author,Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email')
    search_fields = ('first_name','last_name','email')


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_display_links = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','book')
    search_fields = ('id','user','book')




admin.site.register(Books, BooksAdmin)
admin.site.register(Language)
admin.site.register(BooksAutor)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
