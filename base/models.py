from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
def upload_to(instance, filename):
    return 'book/{filename}'.format(filename=filename)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2)
    # image = models.ImageField(upload_to=upload_to ,null=True, default="avatar.svg")
    image = CloudinaryField('image')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
    

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    outstanding_debt = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    rent_fee_charged = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        # return f"{self.book.title} - {self.member.name}"
        return "{} - {}".format(self.book.title, self.member.name)
