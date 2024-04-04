from django.urls import path
from .views import UsersView,UsersDetailView,AddCommentView


app_name = 'users'

urlpatterns = [
    path('list/', UsersView.as_view(), name='list'),
    path('detail/<int:pk>', UsersDetailView.as_view(), name='detail'),
    path('add-comment/<int:pk>', AddCommentView.as_view(), name='add_comment'),
]