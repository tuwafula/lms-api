from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.


# Book views start here
class ListBookView(ListAPIView):
    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CreateBookView(CreateAPIView):
    model = Book
    serializer_class = BookSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

class BookDetailView(RetrieveAPIView):
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
        
# Member views start here
class ListMemberView(ListAPIView):
    pass