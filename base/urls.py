from django.urls import path
from .views import CreateBookView, ListBookView, BookDetailView, BookUpdateView, BookDeleteView, ListMemberView, CreateMemberView, MemberDetailView, MemberUpdateView, MemberDeleteView, ListTransactions,CreateTransaction, TransactionDetailView, TransactionUpdate, TransactionDeleteView


urlpatterns = [
    path('books/', ListBookView.as_view(), name='book_list'),
    path('create-book', CreateBookView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book-update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book-delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),

    path('members', ListMemberView.as_view(), name='member_list'),
    path('create-member', CreateMemberView.as_view(), name='member_detail'),
    path('member/<int:pk>', MemberDetailView.as_view(), name='member_detail'),
    path('member-update/<int:pk>', MemberUpdateView.as_view(), name='member_update'),
    path('member-delete/<int:pk>', MemberDeleteView.as_view(), name='member_delete'),

    path('transactions', ListTransactions.as_view(), name='transaction_list'),
    path('create-transaction', CreateTransaction.as_view()),
    path('transaction/<int:pk>', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transaction-update/<int:pk>', TransactionUpdate.as_view(), name='transaction_update'),
    path('transaction-delete/<int:pk>', TransactionDeleteView.as_view(), name='transaction_delete'),
]