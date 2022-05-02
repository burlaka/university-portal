from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('books/', views.BookListView.as_view()),
	path('books/<slug:pk>/', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/<slug:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]

#urlpatterns += [
#    path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#]
