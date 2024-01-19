from django.db import transaction
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer
from .models import Book, Member, Transaction
from rest_framework import filters
from rest_framework import permissions

# Create your views here.


# Book views start here
class ListBookView(ListAPIView):
    model = Book
    serializer_class = BookSerializer
    search_fields = ['title', 'author']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()

class CreateBookView(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    model = Book
    serializer_class = BookSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetailView(RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookSerializer

    def get_object(self):
        try:
            book = Book.objects.get(id=self.kwargs['pk'])
            if book:
                return book
        except Book.DoesNotExist:
            return None

        return super().get_object()
    
    def get(self, request, *args, **kwargs):
        book = self.get_object()

        if book is not None:
            serializer = self.serializer_class(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail' : 'Book Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

class BookUpdateView(UpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookSerializer

    def get_object(self):
        try:
            book = Book.objects.get(id=self.kwargs['pk'])
            if book:
                return book
        except Book.DoesNotExist:
            return None
        
        return super().get_object()
    
    def put(self, request, *args, **kwargs):
        book = self.get_object()

        if book:
            try:
                serializer = self.serializer_class(instance=book,data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'detail': 'Update failed'}, status=status.HTTP_400_BAD_REQUEST )
                
        else:
            return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# Simplified version of BookUpdateView

# class BookUpdateView(RetrieveUpdateAPIView):
#     # permission_classes = (permissions.IsAdminUser,)
#     serializer_class = BookSerializer

#     def get_object(self):
#         id = self.kwargs['pk']
#         return get_object_or_404(Book, id=id)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


class BookDeleteView(DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        try:
            book = Book.objects.get(id=self.kwargs['pk'])
            if book:
                return book
        except Book.DoesNotExist:
            return None
        
        return super().get_object()
    
    def delete(self, request, *args, **kwargs):
        book = self.get_object()

        if book:
            book.delete()
            return Response({'message': 'success'}, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response({"message": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)
        

##########################################################################################
################################################################################
###################################################################
###########################################

# Member views start here
class ListMemberView(ListAPIView):
    model = Member
    serializer_class = MemberSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Member.objects.all()

class CreateMemberView(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class MemberDetailView(RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Member
    serializer_class = MemberSerializer
    
    def get_object(self):
        try:
            member = Member.objects.get(id=self.kwargs['pk'])
            if member:
                return member
        except Member.DoesNotExist:
            return None
        
        return super().get_object()

    def get(self, request, *args, **kwargs):
        member = self.get_object()

        if member:
            serializer = self.serializer_class(member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Member does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

class MemberUpdateView(RetrieveUpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Member
    serializer_class = MemberSerializer
    
    def get_object(self):
        try:
            member = Member.objects.get(id=self.kwargs['pk'])
            if member:
                return member
        except Member.DoesNotExist:
            return None
        
        return super().get_object()
    
    def put(self, request, *args, **kwargs):
        member = self.get_object()

        if member:
            serializer = self.serializer_class(instance=member, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)
        
class MemberDeleteView(DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Member
    serializer_class = MemberSerializer

    def get_object(self):
        try:
            member = Member.objects.get(id=self.kwargs['pk'])
            if member: 
                return member
        except Member.DoesNotExist:
            return None
        
        return super().get_object()
    
    def delete(self, request, *args, **kwargs):
        member = self.get_object()

        if member:
            member.delete()
            return Response({'message': 'success'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Member does not exist"}, status=status.HTTP_404_NOT_FOUND)


##########################################################################################
################################################################################
###################################################################
###########################################

# Transaction Views start here
class ListTransactions(ListAPIView):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class CreateTransaction(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Transaction
    serializer_class = TransactionSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class TransactionDetailView(RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Transaction
    serializer_class = TransactionSerializer

    def get_object(self):
        try:
            transaction = Transaction.objects.get(id=self.kwargs['pk'])

            if transaction:
                return transaction 
        except Transaction.DoesNotExist:
            return None

        return super().get_object()
    
    def get(self, request, *args, **kwargs):
        transaction = self.get_object()

        if transaction:
            serializer = self.serializer_class(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Transaction does exist'})
        

# class TransactionUpdate(UpdateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     model = Transaction
#     serializer_class = TransactionSerializer

#     def get_object(self):
#         try: 
#             transaction = Transaction.objects.get(id=self.kwargs['pk'])
#             if transaction:
#                 return transaction
#         except Transaction.DoesNotExist:
#             return None
        
#         return super().get_object()
    
#     def put(self, request, *args, **kwargs):
#         transaction = self.get_object()

#         if transaction:
#             serializer = self.serializer_class(instance=transaction, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else: 
#             return Response({"message":"Transaction does not exist"})


# class TransactionUpdate(RetrieveUpdateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer

#     @transaction.atomic
#     def update_transaction(self,request, *args, **kwargs):
#         transaction_instance = self.get_object()
#         transaction_serializer = self.get_serializer(transaction_instance, data=request.data,partial=True)
#         transaction_serializer.is_valid(raise_exception=True)
#         transaction_serializer.save()

#         member_instance = transaction_instance.member
#         member_data = request.data.get('member', {})
#         member_serializer = MemberSerializer(member_instance, data=member_data, partial=True)
#         member_serializer.is_valid(raise_exception=True)
#         member_serializer.save()

#         book_data = request.data.get('book', {})
#         if book_data:
#             book_instance = transaction_instance.book
#             book_serializer = BookSerializer(book_instance, data=book_data, partial=True)
#             book_serializer.is_valid(raise_exception=True)
#             book_serializer.save()

#         return Response(transaction_serializer.data)


class TransactionUpdate(RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        member_data = request.data.get('member', {})
        if member_data:
            member_instance = instance.member
            member_serializer = MemberSerializer(member_instance, data=member_data, partial=True)
            member_serializer.is_valid(raise_exception=True)
            member_serializer.save()

        book_data = request.data.get('book', {})
        if book_data:
            book_instance = instance.book
            book_serializer = BookSerializer(book_instance, data=book_data, partial=True)
            book_serializer.is_valid(raise_exception=True)
            book_serializer.save()

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

        
class TransactionDeleteView(DestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Transaction
    serializer_class = TransactionSerializer

    def get_object(self):
        try: 
            transaction = Transaction.objects.get(id=self.kwargs['pk'])
            if transaction:
                return transaction
        except Transaction.DoesNotExist:
            return None
        
        return super().get_object()

    def delete(self, request, *args, **kwargs):
        transaction = self.get_object()

        if transaction:
            transaction.delete()
            return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Transaction does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
        