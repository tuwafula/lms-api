from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Book, Member, Transaction
from datetime import date

class APITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        
        # Create a book
        cls.book = Book.objects.create(
        title="Django for APIs",
        author="William S. Vincent",
        quantity = 12,
        stock = 12,
        rent_fee = 30,
        image = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwsvincent.com%2Fdjango-for-professionals-40-update%2F&psig=AOvVaw2AQ-XZ1PvdEOsfipbdyKSL&ust=1710763027177000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOit7Iaf-4QDFQAAAAAdAAAAABAE'
        )

        # Create a member
        cls.member = Member.objects.create(
            name='Valerie Ijeji',
            email='val@gmail.com',
            outstanding_debt='0.00'
        )

        # Create a Transaction
        cls.transaction = Transaction.objects.create(
            book=cls.book,
            member=cls.member,
            issue_date=date.today(),
            return_date= None,
            is_returned = False,
            rent_fee_charged = '0.00'
        )


    # Book Tests
    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)


    def test_get_book_detail(self):
        response = self.client.get(reverse("book_detail", kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['author'], self.book.author)
        self.assertEqual(response.data['image'], "image/upload/" + self.book.image)

    def test_update_book(self):
        updated_data = {
            'title': 'Django for Apis',
            'author': 'William S. Vincent',
            'quantity': 15,
            'stock': 15,
            'rent_fee': 40
        }
        response = self.client.put(reverse("book_update", kwargs={'pk': self.book.pk}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])
        self.assertEqual(self.book.author, updated_data['author'])
        self.assertEqual(self.book.quantity, updated_data['quantity'])
        self.assertEqual(self.book.stock, updated_data['stock'])
        self.assertEqual(self.book.rent_fee, updated_data['rent_fee'])

    def test_delete_book(self):
        response = self.client.delete(reverse("book_delete", kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Member Tests
    def test_api_list_member_view(self):
        response = self.client.get(reverse("member_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Member.objects.count(), 1)
        self.assertContains(response, self.member)

    def test_get_member_detail(self):
        response = self.client.get(reverse("member_detail", kwargs={'pk': self.member.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.member.name)
        self.assertEqual(response.data['email'], self.member.email)
        self.assertEqual(response.data['outstanding_debt'], self.member.outstanding_debt)
    
    def test_update_member(self):
        updated_data = {
            'name': 'Valerie Gumanyi',
            'email': 'val@gmail.com',
            'outstanding_debt': 15,
        }
        response = self.client.put(reverse("member_update", kwargs={'pk': self.member.pk}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.member.refresh_from_db()
        self.assertEqual(self.member.name, updated_data['name'])
        self.assertEqual(self.member.email, updated_data['email'])
        self.assertEqual(self.member.outstanding_debt, updated_data['outstanding_debt'])
      
    def test_delete_member(self):
        response = self.client.delete(reverse("member_delete", kwargs={'pk': self.member.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Member.objects.count(), 0)

    # Transaction Tests
    def test_api_list_transaction_view(self):
        response = self.client.get(reverse("transaction_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertContains(response, self.transaction.book.title)
        self.assertContains(response, self.transaction.member.name)

    def test_get_transaction_detail(self):
        response = self.client.get(reverse("transaction_detail", kwargs={'pk': self.transaction.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_book_title = response.data['book']['title']
        self.assertEqual(response_book_title, self.transaction.book.title)

        response_member_name = response.data['member']['name']
        self.assertEqual(response_member_name, self.transaction.member.name)

        self.assertEqual(response.data['is_returned'], self.transaction.is_returned)
        self.assertEqual(response.data['rent_fee_charged'], self.transaction.rent_fee_charged)

    # def test_update_transaction(self):
    #     updated_data = {
    #         'book': self.book.pk,  # Use primary key of the book
    #         'member': self.member.pk,  # Use primary key of the member
    #         # 'issue_date': datetime.datetime.now(),
    #         'return_date': date.today(),
    #         'is_returned': False,
    #         'rent_fee_charged': 40
    #     }
    #     response = self.client.put(reverse("transaction_update", kwargs={'pk': self.transaction.pk}), updated_data)
    #     # self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.transaction.refresh_from_db()
    #     self.assertEqual(self.transaction.book.pk, updated_data['book'])
    #     self.assertEqual(self.transaction.member.pk, updated_data['member'])
    #     # self.assertEqual(self.transaction.issue_date, updated_data['issue_date'])
    #     self.assertEqual(self.transaction.return_date, updated_data['return_date'])
    #     self.assertEqual(self.transaction.is_returned, updated_data['is_returned'])
    #     self.assertEqual(self.transaction.rent_fee_charged, updated_data['rent_fee_charged'])

    def test_delete_transaction(self):
        response = self.client.delete(reverse("transaction_delete", kwargs={'pk': self.transaction.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 0)