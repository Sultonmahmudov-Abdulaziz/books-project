from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Books,Comment
from books.forms import CommentForm


class UsersView(View):
    def get(self,request):

        book = Books.objects.all()

        return render(request,template_name='users/list.html',context={'book':book})
    

class UsersDetailView(View):
    def get(self,request,pk):
        form = CommentForm()
        book = get_object_or_404(Books,pk=pk)
        comments = Comment.objects.filter(book=book)

        return render(request,template_name='users/detail.html',context={'book':book, 'form':form,"comments":comments})

class AddCommentView(LoginRequiredMixin,View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            book = Books.objects.get(id=pk)
            Comment.objects.create(
                user=request.user,
                book=book,
                comment_text=form.cleaned_data['comment_text'],
                stars_given=form.cleaned_data['stars_given'],
            )
            return redirect(reverse('users:detail', kwargs={'pk': book.id}))
        return render(request, 'users/detail.html', {'book': book, 'form': form})


