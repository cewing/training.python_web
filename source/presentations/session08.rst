**********
Session 08
**********

.. figure:: /_static/django-pony.png
    :align: center
    :width: 60%

    image: http://djangopony.com/

Building a Django Application
=============================

.. rst-class:: large

Wherein we build a simple blogging app.


A Full Stack Framework
----------------------

Django comes with:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Persistence via the *Django ORM*
    * CRUD content editing via the automatic *Django Admin*
    * URL Mapping via *urlpatterns*
    * Templating via the *Django Template Language*
    * Caching with levels of configurability
    * Internationalization via i18n hooks
    * Form rendering and handling
    * User authentication and authorization

    Pretty much everything you need to make a solid website quickly

.. nextslide:: What Sets it Apart?

Lots of frameworks offer some of these features, if not all.

.. rst-class:: build
.. container::

    What is Django's *killer feature*

    .. rst-class:: centered

    **The Django Admin**

.. nextslide:: The Django Admin

Works in concert with the Django ORM to provide automatic CRUD functionality

.. rst-class:: build
.. container::

    You write the models, it provides the UI

    You've seen this in action. Pretty neat, eh?

.. nextslide:: The Pareto Principle

The Django Admin is a great example of the Pareto Priciple, a.k.a. the 80/20
rule:

.. rst-class:: build
.. container::

    .. rst-class:: centered

    **80% of the problems can be solved by 20% of the effort**

    The converse also holds true:

    .. rst-class:: centered

    **Fixing the last 20% of the problems will take the remaining 80% of the
    effort.**

.. nextslide:: Other Django Advantages

.. ifnotslides::

    **Other Django Advantages**

Clearly the most popular full-stack Python web framework at this time

.. rst-class:: build
.. container::

    Popularity translates into:

    .. rst-class:: build

    * Active, present community
    * Plethora of good examples to be found online
    * Rich ecosystem of *apps* (encapsulated add-on functionality)

    .. rst-class:: centered

    **Jobs**

.. nextslide:: Active Development

Django releases in the last 12+ months (a short list):

.. rst-class:: build

* 1.7.4 (January 2015)
* 1.6.9 (January 2015)
* 1.7.1 (October 2014)
* 1.6.7 (September 2014)
* 1.7 (September 2014)
* 1.6.5 (May 2014)
* 1.6.2 (February 2014)
* 1.6 (November 2013)

.. nextslide:: Great Documentation

Thorough, readable, and discoverable.

.. rst-class:: build
.. container::

    Led the way to better documentation for all Python

    `Read The Docs <https://readthedocs.org/>`_ - built in connection with
    Django, sponsored by the Django Software Foundation.

    Write documentation as part of your python package.

    Render new versions of that documentation for every commit.

    .. rst-class:: centered

    **this is awesome**


Where We Stand
--------------

For your homework this week, you created a ``Post`` model to serve as the heart
of our blogging app.

.. rst-class:: build
.. container::

    You also took some time to get familiar with the basic workings of the
    Django ORM.

    You made a minor modification to our model class and wrote a test for it.

    And you installed the Django Admin site and added your app to it.


Going Further
-------------

One of the most common features in a blog is the ability to categorize posts.

.. rst-class:: build
.. container::

    Let's add this feature to our blog!

    To do so, we'll be adding a new model, and making some changes to existing
    code.

    .. rst-class:: build

    This means that we'll need to *change our database schema*.


.. nextslide:: Changing a Database

You've seen how to add new tables to a database using the ``migrate`` command.

.. rst-class:: build
.. container::

    And you've created your first migration in setting up the ``Post`` model.

    This is an example of altering the *database schema* using Python code.

    Starting in Django 1.7, this ability is available built-in to Django.

    Before verson 1.7 it was available in an add-on called `South`_.

.. _South: http://south.readthedocs.org/en/latest


.. nextslide:: Adding a Model

We want to add a new model to represent the categories our blog posts might
fall into.

.. rst-class:: build
.. container::

    This model will need to have:

    .. rst-class:: build

    * a name for the category
    * a longer description
    * a relationship to the Post model

    .. code-block:: python

        # in models.py
        class Category(models.Model):
            name = models.CharField(max_length=128)
            description = models.TextField(blank=True)
            posts = models.ManyToManyField(Post, blank=True, null=True,
                                           related_name='categories')


.. nextslide:: Strange Relationships

In our ``Post`` model, we used a ``ForeignKeyField`` field to match an author
to her posts.

.. rst-class:: build
.. container::

    This models the situation in which a single author can have many posts,
    while each post has only one author.

    We call this a *Many to One* relationship.

    But any given ``Post`` might belong in more than one ``Category``.

    And it would be a waste to allow only one ``Post`` for each ``Category``.

    Enter the ``ManyToManyField``

.. nextslide:: Add a Migration

To get these changes set up, we now add a new migration.

.. rst-class:: build
.. container::

    We use the ``makemigrations`` management command to do so:

    .. code-block:: bash

        (djangoenv)$ python manage.py makemigrations
        Migrations for 'myblog':
          0002_category.py:
            - Create model Category

.. nextslide:: Apply A Migration

Once the migration has been created, we can apply it with the ``migrate``
management command.

.. rst-class:: build
.. container::

    .. code-block:: bash

        (djangoenv)$ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, myblog, contenttypes, auth, sessions
        Running migrations:
          Applying myblog.0002_category... OK

    You can even look at the migration file you just applied,
    ``myblog/migrations/0002_category.py`` to see what happened.


.. nextslide:: Make Categories Look Nice

Let's make ``Category`` object look nice the same way we did with ``Post``.
Start with a test:

.. rst-class:: build
.. container::

    add this to ``tests.py``:

    .. code-block:: python

        # another import
        from myblog.models import Category

        # and the test case and test
        class CategoryTestCase(TestCase):

            def test_unicode(self):
                expected = "A Category"
                c1 = Category(name=expected)
                actual = unicode(c1)
                self.assertEqual(expected, actual)

.. nextslide:: Make it Pass

When you run your tests, you now have two, and one is failing because the
``Category`` object doesn't look right.

.. rst-class:: build
.. container::

    .. code-block:: bash

        (djangoenv)$ python manage.py test myblog
        Creating test database for alias 'default'...
        ...

        Ran 2 tests in 0.011s

        FAILED (failures=1)

    Do you remember how you made that change for a ``Post``?

    .. code-block:: python

        class Category(models.Model):
            #...

            def __unicode__(self):
                return self.name


.. nextslide:: Admin for Categories

Adding our new model to the Django admin is equally simple.

.. rst-class:: build
.. container::

    Simply add the following line to ``myblog/admin.py``

    .. code-block:: python

        # a new import
        from myblog.models import Category

        # and a new admin registration
        admin.site.register(Category)


.. nextslide:: Test It Out

Fire up the Django development server and see what you have in the admin:

.. code-block:: bash

    (djangoenv)$ python manage.py runserver
    Validating models...
    ...
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

.. rst-class:: build
.. container::

    Point your browser at ``http://localhost:8000/admin/``, log in and play.

    Add a few categories, put some posts in them. Visit your posts, add new
    ones and then categorize them.


BREAK TIME
----------

We've completed a data model for our application.

And thanks to Django's easy-to-use admin, we have a reasonable CRUD application
where we can manage blog posts and the categories we put them in.

When we return, we'll put a public face on our new creation.

If you've fallen behind, the app as it stands now is in our class resources as
``mysite_stage_1``


A Public Face
=============

.. rst-class:: left

Point your browser at http://localhost:8000/

.. rst-class:: build left
.. container::

    What do you see?

    Why?

    We need to add some public pages for our blog.

    In Django, the code that builds a page that you can see is called a *view*.


Django Views
------------

A *view* can be defined as a *callable* that takes a request and returns a
response.

.. rst-class:: build
.. container::

    This should sound pretty familiar to you.

    Classically, Django views were functions.

    Version 1.3 added support for Class-based Views (a class with a
    ``__call__`` method is a callable)


.. nextslide:: A Basic View

Let's add a really simple view to our app.

.. rst-class:: build
.. container::

    It will be a stub for our public UI.  Add this to ``views.py`` in
    ``myblog``

    .. code-block:: python

        from django.http import HttpResponse, HttpResponseRedirect, Http404

        def stub_view(request, *args, **kwargs):
            body = "Stub View\n\n"
            if args:
                body += "Args:\n"
                body += "\n".join(["\t%s" % a for a in args])
            if kwargs:
                body += "Kwargs:\n"
                body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
            return HttpResponse(body, content_type="text/plain")

.. nextslide:: Hooking It Up

In your homework tutorial, you learned about Django **urlconfs**

.. rst-class:: build
.. container::

    We used our project urlconf to hook the Django admin into our project.

    We want to do the same thing for our new app.

    In general, an *app* that serves any sort of views should contain its own
    urlconf.

    The project urlconf should mainly *include* these where possible.


.. nextslide:: Adding A Urlconf

Create a new file ``urls.py`` inside the ``myblog`` app package.

.. rst-class:: build
.. container::

    Open it in your editor and add the following code:

    .. code-block:: python


        from django.conf.urls import patterns, url

        urlpatterns = patterns('myblog.views',
            url(r'^$',
                'stub_view',
                name="blog_index"),
        )


.. nextslide:: A Word On Prefixes

The ``patterns`` function takes a first argument called the *prefix*

.. rst-class:: build
.. container::

    When it is not empty, it is added to any view names in ``url()`` calls in
    the same ``patterns``.

    In a root urlconf like the one in ``mysite``, this isn't too useful.

    But in ``myblog.urls`` it lets us refer to views by simple function name.

    No need to import every view.

    Nor do we need to reference each by the app and module name where it
    appears.

    This is a convenience.


.. nextslide:: Include Blog Urls

In order for our new urls to load, we'll need to include them in our project
urlconf

.. rst-class:: build
.. container::

    Open ``urls.py`` from the ``mysite`` project package and add this:

    .. code-block:: python


        urlpatterns = patterns('',
            url(r'^', include('myblog.urls')), #<- add this
            #... other included urls
        )

    Try reloading http://localhost:8000/

    You should see some output now.


Project URL Space
-----------------

A project is defined by the urls a user can visit.

.. rst-class:: build
.. container::

    What should our users be able to see when they visit our blog?

    .. rst-class:: build

    * A list view that shows blog posts, most recent first.
    * An individual post view, showing a single post (a permalink).

    Let's add urls for each of these.

    For now, we'll use the stub view we've created so we can concentrate on the
    url routing.

.. nextslide:: Our URLs

We've already got a good url for the list page: ``blog_index`` at '/'

.. rst-class:: build
.. container::

    For the view of a single post, we'll need to capture the id of the post.
    Add this to ``urlpatterns`` in ``myblog/urls.py``:

    .. code-block:: python

        url(r'^posts/(\d+)/$',
            'stub_view',
            name="blog_detail"),

    ``(\d+)`` captures one or more digits as the post_id.

    Load http://localhost:8000/posts/1234/ and see what you get.

.. nextslide:: A Word on Capture in URLs

When you load the above url, you should see ``1234`` listed as an *arg*

.. rst-class:: build
.. container::

    Try changing the route like so:

    .. code-block:: python

        r'^posts/(?P<post_id>\d+)/$'

    Reload the same url.

    Notice the change.

    What's going on there?

.. nextslide:: Regular Expression URLS

Like Pyramid, Django uses Python regular expressions to build routes.

.. rst-class:: build
.. container::

    Unlike Pyramid, Django *requires* regular expressions to capture segments
    in a route.

    When we built our WSGI book app, we used this same appraoch.

    There we learned about regular expression *capture groups*. We just changed
    an unnamed *capture group* to a named one.

    How you declare a capture group in your url pattern regexp influences how
    it will be passed to the view callable.


.. nextslide:: Full Urlconf

.. code-block:: python


    from django.conf.urls import patterns, url

    urlpatterns = patterns('myblog.views',
        url(r'^$',
            'stub_view',
            name="blog_index"),
        url(r'^posts/(?P<post_id>\d+)/$',
            'stub_view',
            name="blog_detail"),
    )


.. nextslide:: Testing Views

Before we begin writing real views, we need to add some tests for the views we
are about to create.

.. rst-class:: build
.. container::

    We'll need tests for a list view and a detail view

    add the following *imports* at the top of ``myblog/tests.py``:

    .. code-block:: python

        import datetime
        from django.utils.timezone import utc


.. nextslide:: Add a Test Case

.. code-block:: python

    class FrontEndTestCase(TestCase):
        """test views provided in the front-end"""
        fixtures = ['myblog_test_fixture.json', ]

        def setUp(self):
            self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
            self.timedelta = datetime.timedelta(15)
            author = User.objects.get(pk=1)
            for count in range(1, 11):
                post = Post(title="Post %d Title" % count,
                            text="foo",
                            author=author)
                if count < 6:
                    # publish the first five posts
                    pubdate = self.now - self.timedelta * count
                    post.published_date = pubdate
                post.save()


Our List View
-------------

We'd like our list view to show our posts.

.. rst-class:: build
.. container::

    But in this blog, we have the ability to publish posts.

    Unpublished posts should not be seen in the front-end views.

    We set up our tests to have 5 published, and 5 unpublished posts

    Let's add a test to demonstrate that the right ones show up.

.. nextslide:: Testing the List View

.. code-block:: python

        Class FrontEndTestCase(TestCase): # already here
            # ...
            def test_list_only_published(self):
                resp = self.client.get('/')
                self.assertTrue("Recent Posts" in resp.content)
                for count in range(1, 11):
                    title = "Post %d Title" % count
                    if count < 6:
                        self.assertContains(resp, title, count=1)
                    else:
                        self.assertNotContains(resp, title)

.. rst-class:: build
.. container::

    We test first to ensure that each published post is visible in our view.

    Note that we also test to ensure that the unpublished posts are *not* visible.


.. nextslide:: Run Your Tests

.. code-block:: bash

    (djangoenv)$ python manage.py test myblog
    Creating test database for alias 'default'...
    .F.
    ======================================================================
    FAIL: test_list_only_published (myblog.tests.FrontEndTestCase)
    ...
    Ran 3 tests in 0.024s

    FAILED (failures=1)
    Destroying test database for alias 'default'...


.. nextslide:: Now Fix That Test!

Add the view for listing blog posts to ``views.py``.

.. code-block:: python

    # add these imports
    from django.template import RequestContext, loader
    from myblog.models import Post

    # and this view
    def list_view(request):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        template = loader.get_template('list.html')
        context = RequestContext(request, {
            'posts': posts,
        })
        body = template.render(context)
        return HttpResponse(body, content_type="text/html")


.. nextslide:: Getting Posts

.. code-block:: python

    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')

.. rst-class:: build
.. container::

    We begin by using the QuerySet API to fetch all the posts that have
    ``published_date`` set

    Using the chaining nature of the API we order these posts by
    ``published_date``

    Remember, at this point, no query has actually been issued to the database.


.. nextslide:: Getting a Template

.. code-block:: python

    template = loader.get_template('list.html')

.. rst-class:: build
.. container::

    Django uses configuration to determine how to find templates.

    By default, Django looks in installed *apps* for a ``templates`` directory

    It also provides a place to list specific directories.

    Let's set that up in ``settings.py``


.. nextslide:: Project Templates

Notice that ``settings.py`` already contains a ``BASE_DIR`` value which points
to the root of our project (where both the project and app packages are
located).

.. rst-class:: build
.. container::

    In that same file add a tuple bound to ``TEMPLATE_DIRS`` and add a path to
    it:

    .. code-block:: python

        TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'mysite/templates'), )

    Then add a ``templates`` directory to your ``mysite`` project package

    Finally, in that directory add a new file ``base.html`` and populate it
    with the following:


.. nextslide:: ``base.html``

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
      <head>
        <title>My Django Blog</title>
      </head>
      <body>
        <div id="container">
          <div id="content">
          {% block content %}
           [content will go here]
          {% endblock %}
          </div>
        </div>
      </body>
    </html>


Templates in Django
-------------------

Before we move on, a quick word about Django templates.

.. rst-class:: build
.. container::

    We've seen Jinja2 which was "inspired by Django's templating system".

    Basically, you already know how to write Django templates.

    Django templates **do not** allow any python expressions.

    https://docs.djangoproject.com/en/1.7/ref/templates/builtins/


.. nextslide:: Blog Templates

Our view tries to load ``list.html``.

.. rst-class:: build
.. container::

    This template is probably specific to the blog functionality of our site

    It is common to keep shared templates in your project directory and
    specialized ones in app directories.

    Add a ``templates`` directory to your ``myblog`` app, too.

    In it, create a new file ``list.html`` and add this:


.. nextslide:: ``list.html``

.. code-block:: jinja

    {% extends "base.html" %}

    {% block content %}
      <h1>Recent Posts</h1>

      {% comment %} here is where the query happens {% endcomment %}
      {% for post in posts %}
      <div class="post">
        <h2>{{ post }}</h2>
        <p class="byline">
          Posted by {{ post.author_name }} &mdash; {{ post.published_date }}
        </p>
        <div class="post-body">
          {{ post.text }}
        </div>
        <ul class="categories">
          {% for category in post.categories.all %}
            <li>{{ category }}</li>
          {% endfor %}
        </ul>
      </div>
      {% endfor %}
    {% endblock %}


.. nextslide:: Template Context

.. code-block:: python

    context = RequestContext(request, {
        'posts': posts,
    })
    body = template.render(context)

.. rst-class:: build
.. container::

    Like Jinja2, django templates are rendered by passing in a *context*

    Django's RequestContext provides common bits, similar to the global context
    in Flask

    We add our posts to that context so they can be used by the template.


.. nextslide:: Return a Response

.. code-block:: python

    return HttpResponse(body, content_type="text/html")

.. rst-class:: build
.. container::

    Finally, we build an HttpResponse and return it.

    This is, fundamentally, no different from the ``stub_view`` just above.

.. nextslide:: Fix URLs

We need to fix the url for our blog index page

.. rst-class:: build
.. container::

    Update ``urls.py`` in ``myblog``:

    .. code-block:: python

        url(r'^$',
            'list_view',
            name="blog_index"),

    Then run your tests again:

    .. code-block:: bash

        (djangoenv)$ python manage.py test myblog
        ...
        Ran 3 tests in 0.033s

        OK


.. nextslide:: Common Patterns

This is a common pattern in Django views:

.. rst-class:: build

* get a template from the loader
* build a context, usually using a RequestContext
* render the template
* return an HttpResponse

.. rst-class:: build
.. container::

    So common in fact that Django provides two shortcuts for us to use:

    .. rst-class:: build

    * ``render(request, template[, ctx][, ctx_instance])``
    * ``render_to_response(template[, ctx][, ctx_instance])``


.. nextslide:: Shorten Our View

Let's replace most of our view with the ``render`` shortcut

.. code-block:: python

    from django.shortcuts import render # <- already there

    # rewrite our view
    def list_view(request):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        context = {'posts': posts}
        return render(request, 'list.html', context)

.. rst-class:: build

Remember though, all we did manually before is still happening


BREAK TIME
----------

We've got the front page for our application working great.

Next, we'll need to provide a view of a detail page for a single post.

Then we'll provide a way to log in and to navigate between the public part of
our application and the admin behind it.

If you've fallen behind, the app as it stands now is in our class resources as
``mysite_stage_2``


Our Detail View
---------------

Next, let's add a view function for the detail view of a post

.. rst-class:: build
.. container::

    It will need to get the ``id`` of the post to show as an argument

    Like the list view, it should only show published posts

    But unlike the list view, it will need to return *something* if an
    unpublished post is requested.

    Let's start with the tests in ``views.py``


.. nextslide:: Testing the Details

Add the following test to our ``FrontEndTestCase`` in ``myblog/tests.py``:

.. code-block:: python

        def test_details_only_published(self):
            for count in range(1, 11):
                title = "Post %d Title" % count
                post = Post.objects.get(title=title)
                resp = self.client.get('/posts/%d/' % post.pk)
                if count < 6:
                    self.assertEqual(resp.status_code, 200)
                    self.assertContains(resp, title)
                else:
                    self.assertEqual(resp.status_code, 404)


.. nextslide:: Run Your Tests

.. code-block:: bash

    (djangoenv)$ python manage.py test myblog
    Creating test database for alias 'default'...
    .F..
    ======================================================================
    FAIL: test_details_only_published (myblog.tests.FrontEndTestCase)
    ...
    Ran 4 tests in 0.043s

    FAILED (failures=1)
    Destroying test database for alias 'default'...


.. nextslide:: Let's Fix That Test

Now, add a new view to ``myblog/views.py``:

.. code-block:: python

    def detail_view(request, post_id):
        published = Post.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        context = {'post': post}
        return render(request, 'detail.html', context)


.. nextslide:: Missing Content

One of the features of the Django ORM is that all models raise a DoesNotExist
exception if ``get`` returns nothing.

.. rst-class:: build
.. container::

    This exception is actually an attribute of the Model you look for.

    There's also an ``ObjectDoesNotExist`` for when you don't know which model
    you have.

    We can use that fact to raise a Not Found exception.

    Django will handle the rest for us.


.. nextslide:: Add the Template

We also need to add ``detail.html`` to ``myblog/templates``:

.. code-block:: jinja

    {% extends "base.html" %}

    {% block content %}
    <a class="backlink" href="/">Home</a>
    <h1>{{ post }}</h1>
    <p class="byline">
      Posted by {{ post.author_name }} &mdash; {{ post.published_date }}
    </p>
    <div class="post-body">
      {{ post.text }}
    </div>
    <ul class="categories">
      {% for category in post.categories.all %}
        <li>{{ category }}</li>
      {% endfor %}
    </ul>
    {% endblock %}


.. nextslide:: Hook it Up

In order to view a single post, we'll need a link from the list view

.. rst-class:: build
.. container::

    We can use the ``url`` template tag (like Pyramid's ``request.route_url``):

    .. code-block:: jinja

        {% url '<view_name>' arg1 arg2 %}

    In our ``list.html`` template, let's link the post titles:

    .. code-block:: jinja

        {% for post in posts %}
        <div class="post">
          <h2>
            <a href="{% url 'blog_detail' post.pk %}">{{ post }}</a>
          </h2>
          ...


.. nextslide:: Fix URLs

Again, we need to insert our new view into the existing ``myblog/urls.py`` in
``myblog``:

.. code-block:: python

    url(r'^posts/(?P<post_id>\d+)/$',
        'detail_view',
        name="blog_detail"),

.. rst-class:: build small

::

    (djangoenv)$ python manage.py test myblog
    ...
    Ran 4 tests in 0.077s

    OK


.. nextslide:: A Moment To Play

We've got some good stuff to look at now.  Fire up the server

.. rst-class:: build
.. container::

    Reload your blog index page and click around a bit.

    You can now move back and forth between list and detail view.

    Try loading the detail view for a post that doesn't exist


.. nextslide:: Congratulations

You've got a functional Blog

.. rst-class:: build
.. container::

    It's not very pretty, though.

    We can fix that by adding some css

    This gives us a chance to learn about Django's handling of *static files*


Static Files
------------

Like templates, Django expects to find static files in particular locations

.. rst-class:: build
.. container::

    It will look for them in a directory named ``static`` in any installed
    apps.

    They will be served from the url path in the STATIC_URL setting.

    By default, this is ``/static/``

    To allow Django to automatically build the correct urls for your static
    files, you use a special *template tag*::

        {% static <filename> %}


.. nextslide:: Add CSS

I've prepared a css file for us to use. You can find it in the class resources

.. rst-class:: build
.. container::

    Create a new directory ``static`` in the ``myblog`` app.

    Copy the ``django_blog.css`` file into that new directory.

    .. container::

        Next, load the static files template tag into ``base.html`` (this must
        be on the first line of the template):

        .. code-block:: jinja

            {% load staticfiles %}

        Finally, add a link to the stylesheet using the special template tag:

        .. code-block:: html

            <title>My Django Blog</title> <!-- This is already present -->
            <link type="text/css" rel="stylesheet" href="{% static 'django_blog.css' %}">


.. nextslide:: View Your Results

Reload http://localhost:8000/ and view the results of your work

.. rst-class:: build
.. container::

    We now have a reasonable view of the posts of our blog on the front end

    And we have a way to create and categorize posts using the admin

    However, we lack a way to move between the two.

    Let's add that ability next.


Global Navigation
-----------------

We'll start by adding a control bar to our ``base.html`` template:

.. code-block:: jinja

    <!DOCTYPE html>
      ...
        <div id="header">
          <ul id="control-bar">
          {% if user.is_authenticated %}
            {% if user.is_staff %}<li>admin</li>{% endif %}
            <li>logout</li>
          {% else %}
            <li>login</li>
          {% endif %}
          </ul>
        </div>
        <div id="container">
          ...


.. nextslide:: Request Context Revisited

When we set up our views, we used the ``render`` shortcut, which provides a
``RequestContext``

.. rst-class:: build
.. container::

    This gives us access to ``user`` in our templates

    It provides access to methods about the state and rights of that user

    We can use these to conditionally display links or UI elements. Like only
    showing the admin link to staff members.


.. nextslide:: Login/Logout

Django also provides a reasonable set of views for login/logout.

.. rst-class:: build
.. container::

    The first step to using them is to hook them into a urlconf.

    .. container::

        Add the following to ``mysite/urls.py``:

        .. code-block:: python

            url(r'^', include('myblog.urls')), #<- already there
            url(r'^login/$',
                'django.contrib.auth.views.login',
                {'template_name': 'login.html'},
                name="login"),
            url(r'^logout/$',
                'django.contrib.auth.views.logout',
                {'next_page': '/'},
                name="logout"),


.. nextslide:: Login Template

We need to create a new ``login.html`` template in ``mysite/templates``:

.. code-block:: jinja

    {% extends "base.html" %}

    {% block content %}
    <h1>My Blog Login</h1>
    <form action="" method="POST">{% csrf_token %}
      {{ form.as_p }}
      <p><input type="submit" value="Log In"></p>
    </form>
    {% endblock %}


.. nextslide:: Submitting Forms

In a web application, submitting forms is potentially hazardous

.. rst-class:: build
.. container::

    Data is being sent to our application from some remote place

    If that data is going to alter the state of our application, we **must**
    use POST

    Even so, we are vulnerable to Cross-Site Request Forgery, a common attack
    vector.


.. nextslide:: Danger: CSRF

Django provides a convenient system to fight this.

.. rst-class:: build
.. container::

    In fact, for POST requests, it *requires* that you use it.

    The Django middleware that does this is enabled by default.

    All you need to do is include the ``{% csrf_token %}`` tag in your form.


.. nextslide:: Hooking It Up

In ``base.html`` make the following updates:

.. rst-class:: build
.. container::

    .. code-block:: jinja

        <!-- admin link -->
        <a href="{% url 'admin:index' %}">admin</a>
        <!-- logout link -->
        <a href="{% url 'logout' %}">logout</a>
        <!-- login link -->
        <a href="{% url 'login' %}">login</a>

    .. container::

        Finally, in ``settings.py`` add the following:

        .. code-block:: python


            LOGIN_URL = '/login/'
            LOGIN_REDIRECT_URL = '/'


.. nextslide:: Forms In Django

In adding a login view, we've gotten a sneak peak at how forms work in Django.

.. rst-class:: build
.. container::

    However, learning more about them is beyond what we can achieve in this
    session.

    The form system in Django is quite nice, however. I urge you to
    `read more about it`_

    In particular, you might want to pay attention to the documentation on
    `Model Forms`_


.. _read more about it: https://docs.djangoproject.com/en/1.6/topics/forms/
.. _Model Forms: https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/


Ta-Daaaaaa!
-----------

So, that's it.  We've created a workable, simple blog app in Django.

.. rst-class:: build
.. container::

    If you fell behind at some point, the app as it now stands is in our class
    resources as ``mysite_stage_3``.

    There's much more we could do with this app. And for homework, you'll do
    some of it.

    Then next session, we'll work together as pairs to implement a simple
    feature to extend the blog


Homework
========

.. rst-class:: left

For your homework this week, we'll fix one glaring problem with our blog admin.

.. rst-class:: build left
.. container::

    As you created new categories and posts, and related them to each-other,
    how did you feel about that work?

    Although from a data perspective, the category model is the right place for
    the ManytoMany relationship to posts, this leads to awkward usage in the
    admin.

    It would be much easier if we could designate a category for a post *from
    the Post admin*.


Your Assignment
---------------

You'll be reversing that relationship so that you can only add categories to
posts

.. rst-class:: build
.. container::

    Take the following steps:

    1. Read the documentation about the `Django admin.`_
    2. You'll need to create a customized `ModelAdmin`_ class for the ``Post``
       and ``Category`` models.
    3. And you'll need to create an `InlineModelAdmin`_ to represent Categories
       on the Post admin view.
    4. Finally, you'll need to `suppress the display`_  of the 'posts' field on
       your ``Category`` admin view.


.. _Django admin.: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/
.. _ModelAdmin: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#modeladmin-objects
.. _InlineModelAdmin: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#inlinemodeladmin-objects
.. _suppress the display: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#modeladmin-options


.. nextslide:: Pushing Further

All told, those changes should not require more than about 15 total lines of
code.

.. rst-class:: build
.. container::

    The trick of course is reading and finding out which fifteen lines to
    write.

    If you complete that task in less than 3-4 hours of work, consider looking
    into other ways of customizing the admin.


.. nextslide:: Tasks you might consider

.. rst-class:: build

* Change the admin index to say 'Categories' instead of 'Categorys'.
* Add columns for the date fields to the list display of Posts.
* Display the created and modified dates for your posts when viewing them in
  the admin.
* Add a column to the list display of Posts that shows the author.  For more
  fun, make this a link that takes you to the admin page for that user.
* For the biggest challenge, look into `admin actions`_ and add an action to
  the Post admin that allows you to bulk publish posts from the Post list
  display

.. _admin actions: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/actions/
