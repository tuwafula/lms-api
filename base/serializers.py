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
            'image': {'required': False}
        }

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

        extra_kwargs = {
            'name': {'required': False},
            'email': {'required': False},
            'email': {'validators': []},
        }
    
    def validate_email(self, value):
        # Check if the email is being updated and another member with the new email already exists
        if self.instance and self.instance.email != value:
            existing_member = Member.objects.filter(email=value)
            if existing_member.exists():
                raise serializers.ValidationError("Member with this email already exists.")
        return value

      

class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()

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