from django.test import TestCase
from user.models import UserModel
from user.models import UserRecoveryModel
import uuid


class UnitTestUserModel(TestCase):

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

    def test_create_an_user_with_a_numeric_phone_number(self):
        #TODO Add validation in the model
        data = {
            'email': 'test@email.com',
            'name': 'test',
            'phone': 00000000000
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertNotEqual(user.phone, 0)
        self.assertEqual(user.phone, '00000000000')

    def test_create_an_user_with_an_invalid_phone_number_lenght(self):

        data = {
            'email': 'test@email.com',
            'name': 'test',
            'phone': '00000000000'
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertEqual(len(user.phone), 11)

    def test_create_an_user_with_a_numeric_name(self):
        #TODO Add validation in the model
        data = {
            'email': 'test@email.com',
            'name': 123
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertNotEqual(user.name, 123)


    def test_create_an_user_with_a_numeric_email(self):
        #TODO Add validation in the model
        data = {
            'email': 123,
            'name': 'teste'
        }

        user = UserModel.objects.create(**data)
        self.assertTrue(isinstance(user, UserModel))
        self.assertNotEqual(user.email, 123)
        self.assertEqual(user.email, '123')


class UnitTestUserRecoveryModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(**{'email': 123, 'name': 'teste'})

    def test_create_an_recovery_code(self):
        id = uuid.uuid4()
        code = UserRecoveryModel.objects.create(**{'id': id, 'user': self.user})
        self.assertEqual(code.id, id)
