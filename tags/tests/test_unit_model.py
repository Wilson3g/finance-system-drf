from django.test import TestCase
from tags.models import TagModel
from user.models import UserModel
import unittest


class UnitTestTagModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(**{'email': 'test@email.com', 'name': 'test'})

    def test_create_a_valid_tag(self):
        tag = TagModel.objects.create(**{'description': 'My description', 'user': self.user})
        self.assertEqual(tag.description, 'My description')
        self.assertTrue(isinstance(tag.description, str))
        self.assertTrue(isinstance(tag.user, UserModel))

    @unittest.expectedFailure
    def test_create_a_tag_without_user(self):
        TagModel.objects.create(**{'description': 'My description'})

    def test_display_tag_data(self):
        tag = TagModel.objects.create(**{'description': 'My description', 'user': self.user})
        self.assertEqual(tag.description, 'My description')

    def test_display_tag_and_user_data(self):
        tag = TagModel.objects.create(**{'description': 'My description', 'user': self.user})
        self.assertEqual(tag.description, 'My description')
        self.assertEqual(tag.user.email, 'test@email.com')
        self.assertEqual(tag.user.phone, None)
        self.assertEqual(tag.user.name, 'test')

    def test_update_tag(self):
        tag = TagModel.objects.create(**{'description': 'My description', 'user': self.user})

        tag.description = 'my updated description'

        self.assertNotEqual(tag.description, 'My description')
        self.assertEqual(tag.description, 'my updated description')
