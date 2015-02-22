from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post, Category


class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_unicode(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = unicode(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_unicode(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = unicode(c1)
        self.assertEqual(expected, actual)
