from django.urls import reverse
from django.test import TestCase
from users.models import User

class UserModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create(
            email='doe@gmail.com',
            password='password',
            first_name='John',
            last_name='Doe',
            avatar='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwsvincent.com%2Fdjango-for-professionals-40-update%2F&psig=AOvVaw2AQ-XZ1PvdEOsfipbdyKSL&ust=1710763027177000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOit7Iaf-4QDFQAAAAAdAAAAABAE'
        )


    def test_user_creation(self):
        self.assertEqual(self.user.email, 'doe@gmail.com')
        self.assertTrue(self.user.password)
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.avatar)



