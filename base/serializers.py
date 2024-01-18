from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Book, Member, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TransactionSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()

    class Meta: 
        model = Transaction
        fields = '__all__'