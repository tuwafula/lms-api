from django.contrib import admin
from .models import Book, Member, Transaction

# Register your models here.
admin.site.register((Book, Member, Transaction,))
