import unittest

from pyramid import testing


class PageModelTests(unittest.TestCase):

    def _getTargetClass(self):
        from .models import Page
        return Page

    def _makeOne(self, data=u'some data'):
        return self._getTargetClass()(data=data)

    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.data, u'some data')


class WikiModelTests(unittest.TestCase):

    def _getTargetClass(self):
        from .models import Wiki
        return Wiki

    def _makeOne(self):
        return self._getTargetClass()()

    def test_it(self):
        wiki = self._makeOne()
        self.assertEqual(wiki.__parent__, None)
        self.assertEqual(wiki.__name__, None)


class AppmakerTests(unittest.TestCase):

    def _callFUT(self, zodb_root):
        from .models import appmaker
        return appmaker(zodb_root)

    def test_it(self):
        root = {}
        self._callFUT(root)
        self.assertEqual(root['app_root']['FrontPage'].data,
                         'This is the front page')
