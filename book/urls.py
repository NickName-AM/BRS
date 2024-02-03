from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-home'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
]