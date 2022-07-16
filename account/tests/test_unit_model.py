from django.test import TestCase
from account.models import AccountModel
from user.models import UserModel
import unittest


class UnitTestAccountModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(**{'email': 'test@email.com', 'name': 'test'})

    def test_create_valid_account(self):
        data = {
            'description': 'my first account',
            'value': 12.99,
            'user': self.user
        }

        account = AccountModel.objects.create(**data)
        self.assertEqual(account.description, 'my first account')
        self.assertEqual(account.value, 12.99)
        self.assertEqual(account.user, self.user)

    def test_create_valid_account_with_pay_type(self):
        data = {
            'description': 'my first account',
            'value': 12.99,
            'user': self.user,
            'type': 'PAY'
        }

        account = AccountModel.objects.create(**data)
        self.assertEqual(account.description, 'my first account')
        self.assertEqual(account.value, 12.99)
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.type, 'PAY')

    def test_create_valid_account_with_pay_receive_type(self):
        data = {
            'description': 'my first account',
            'value': 12.99,
            'user': self.user,
            'type': 'REC'
        }

        account = AccountModel.objects.create(**data)
        self.assertEqual(account.description, 'my first account')
        self.assertEqual(account.value, 12.99)
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.type, 'REC')

    @unittest.expectedFailure
    def test_create_account_with_invalid_type(self):
        data = {
            'description': 'my first account',
            'value': 12.99,
            'user': self.user,
            'type': 'RECEIVE'
        }
        AccountModel.objects.create(**data)

    def test_update_account(self):
        data = {'description': 'my first account','value': 12.99,'user': self.user,'type': 'REC'}
        account = AccountModel.objects.create(**data)

        account.description = 'updated description'
        account.value = 109.99
        account.type = 'PAY'
        account.save()

        self.assertNotEqual(account.description, 'my first account')
        self.assertNotEqual(account.value, 12.99)
        self.assertNotEqual(account.type, 'REC')
        self.assertEqual(account.description, 'updated description')
        self.assertEqual(account.value, 109.99)
        self.assertEqual(account.type, 'PAY')

    def test_display_account_info(self):
        data = {'description': 'my first account','value': 12.99,'user': self.user,'type': 'REC'}
        account = AccountModel.objects.create(**data)
        self.assertEqual(account.description, 'my first account')
        self.assertEqual(account.value, 12.99)
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.type, 'REC')
        self.assertEqual(account.user.name, self.user.name)
        self.assertEqual(account.user.email, self.user.email)
        self.assertEqual(account.user.phone, self.user.phone)
