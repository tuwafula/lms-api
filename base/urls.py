from django.urls import path
from .views import CreateBookView, ListBookView, BookDetailView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('create-book', CreateBookView.as_view()),
    path('books', ListBookView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('book-update/<int:pk>', BookUpdateView.as_view()),
    path('book-delete/<int:pk>', BookDeleteView.as_view()),
]