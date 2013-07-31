import datetime
from django.test import TestCase
from django.utils.timezone import utc
from djagno.contrib.auth.models import User

from myblog.models import Post, Category


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

    def test_category_only_published(self):
        resp = self.client.get('/category/%d/' % self.category.pk)
        for count in range(1,11):
            title = "Post %d Title" % count
            if count < 6 and bool(count & 1):
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)