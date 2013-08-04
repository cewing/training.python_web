import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django.utils.timezone import utc

from myblog.models import Post
from myblog.models import Category
from myblog.admin import PostAdmin


class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_unicode(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = unicode(p1)
        self.assertEqual(expected, actual)

    def test_author_name(self):
        for author in User.objects.all():
            fn, ln, un = (author.first_name, author.last_name,
                          author.username)
            author_name = Post(author=author).author_name()
            if not (fn and ln):
                self.assertEqual(author_name, un)
            else:
                if fn:
                    self.assertTrue(fn in author_name)
                if ln:
                    self.assertTrue(ln in author_name)


class CategoryTestCase(TestCase):

    def test_unicode(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = unicode(c1)
        self.assertEqual(expected, actual)


class PostAdminTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]
    
    def setUp(self):
        admin = AdminSite()
        self.ma = PostAdmin(Post, admin)
        for author in User.objects.all():
            title = "%s's title" % author.username
            post = Post(title=title, author=author)
            post.save()
        self.client.login(username='admin', password='secret')

    def test_author_link(self):
        expected_link_path = '/admin/auth/user/%s'
        for post in Post.objects.all():
            expected = expected_link_path % post.author.pk
            actual = self.ma.author_link(post)
            self.assertTrue(expected in actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['myblog_test_fixture.json', ]
    
    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        self.category = Category(name='A Category')
        self.category.save()
        for count in range(1,11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()
            if bool(count & 1):
                # put odd items in category:
                self.category.posts.add(post)

    def test_list_only_published(self):
        resp = self.client.get('/')
        self.assertTrue("Recent Posts" in resp.content)
        for count in range(1,11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1,11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
