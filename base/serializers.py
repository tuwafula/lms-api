# from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Book, Member, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        extra_kwargs = {
            'title': {'required': False},
            'author': {'required': False},
            'quantity': {'required': False},
            'stock': {'required': False},
            'rent_fee': {'required': False},

           
        }

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

        extra_kwargs = {
            'name': {'required': False},
            'email': {'required': False},
        }

class TransactionSerializer(serializers.ModelSerializer):
    book = BookSerializer(required=False)
    member = MemberSerializer(required=False)

    class Meta: 
        model = Transaction
        fields = '__all__'

    def update(self, instance, validated_data):
        # Handle nested serializer updates manually
        book_data = validated_data.pop('book', {})
        if book_data:
            book_instance = instance.book
            book_serializer = BookSerializer(book_instance, data=book_data, partial=True)
            book_serializer.is_valid(raise_exception=True)
            book_serializer.save()

        member_data = validated_data.pop('member', {})
        if member_data:
            member_instance = instance.member
            member_serializer = MemberSerializer(member_instance, data=member_data, partial=True)
            member_serializer.is_valid(raise_exception=True)
            member_serializer.save()

        # Call the default .update() method for other fields
        return super().update(instance, validated_data)