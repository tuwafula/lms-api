from django.urls import path
from .views import CreateBookView, ListBookView, BookDetailView, BookUpdateView, BookDeleteView, ListMemberView, CreateMemberView, MemberDetailView, MemberUpdateView, MemberDeleteView, ListTransactions,CreateTransaction, TransactionDetailView, TransactionUpdate, TransactionDeleteView


urlpatterns = [
    path('books/', ListBookView.as_view()),
    path('create-book', CreateBookView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('book-update/<int:pk>', BookUpdateView.as_view()),
    path('book-delete/<int:pk>', BookDeleteView.as_view()),

    path('members', ListMemberView.as_view()),
    path('create-member', CreateMemberView.as_view()),
    path('member/<int:pk>', MemberDetailView.as_view()),
    path('member-update/<int:pk>', MemberUpdateView.as_view()),
    path('member-delete/<int:pk>', MemberDeleteView.as_view()),

    path('transactions', ListTransactions.as_view()),
    path('create-transaction', CreateTransaction.as_view()),
    path('transaction/<int:pk>', TransactionDetailView.as_view()),
    path('transaction-update/<int:pk>', TransactionUpdate.as_view()),
    path('transaction-delete/<int:pk>', TransactionDeleteView.as_view()),
]