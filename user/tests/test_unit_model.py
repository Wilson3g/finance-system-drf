from django.test import TestCase
from user.models import UserModel
from user.models import UserRecoveryModel
import uuid
import unittest


class UnitTestUserModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(**{'email': 'test_user@email.com', 'name': 'test_user'})

    def test_create_a_valid_user(self):

        data = {
            'email': 'test@email.com',
            'name': 'test',
            'phone': '00000000000'
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertEqual(user.email, 'test@email.com')
        self.assertEqual(user.name, 'test')
        self.assertEqual(user.phone, '00000000000')

    def test_create_an_user_without_phone_number(self):

        data = {
            'email': 'test@email.com',
            'name': 'test'
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertEqual(user.phone, None)

    def test_create_an_user_with_a_blank_phone_number(self):

        data = {
            'email': 'test@email.com',
            'name': 'test',
            'phone': ''
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertEqual(user.phone, '')

    def test_update_user(self):
        user_old_email = self.user.email
        user_old_name = self.user.name
        user_old_phone = self.user.phone

        self.user.email = 'test_update@email.com'
        self.user.name = 'test_update'
        self.user.phone = '00000000000'
        self.user.save()

        self.assertNotEqual(self.user.email, user_old_email)
        self.assertNotEqual(self.user.name, user_old_name)
        self.assertNotEqual(self.user.phone, user_old_phone)

    def test_delete_user(self):
        self.assertTrue(isinstance(self.user, UserModel))
        user = self.user.delete()
        self.assertEqual(user, None)

    @unittest.expectedFailure
    def test_create_an_user_with_an_existent_email(self):
        UserModel.objects.create(email="test_user@email.com")
        self.user.email = 'test_update@email.com'

    @unittest.expectedFailure
    def test_update_an_user_with_an_existent_email(self):
        user = UserModel.objects.create(**{'email': 'test@email.com', 'name': 'test', 'phone': ''})
        user.email = 'test_user@email.com'
        user.save()

    def test_display_user_info(self):
        self.assertEqual(self.user.email, 'test_user@email.com')
        self.assertEqual(self.user.name, 'test_user')


class UnitTestUserRecoveryModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(**{'email': 'test@email.com', 'name': 'test'})

    def test_create_an_recovery_code(self):
        id = uuid.uuid4()
        code = UserRecoveryModel.objects.create(**{'id': id, 'user': self.user})
        self.assertEqual(code.id, id)
