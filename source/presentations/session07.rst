Python Web Programming
======================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Session 7: A Django Application

.. class:: intro-blurb right

Wherein we build a simple blogging app.

.. class:: image-credit

image: http://djangopony.com/


Full Stack Framework
--------------------

Django comes with:

.. class:: incremental

* Persistence via the *Django ORM*
* CRUD content editing via the automatic *Django Admin*
* URL Mapping via *urlpatterns*
* Templating via the *Django Template Language*
* Caching with levels of configurability
* Internationalization via i18n hooks
* Form rendering and handling
* User authentication and authorization 

.. class:: incremental

Pretty much everything you need to make a solid website quickly


What Sets it Apart?
-------------------

Lots of frameworks offer some of these features, if not all.

.. class:: incremental

What is Django's *killer feature*

.. class:: incremental center

**The Django Admin**


The Django Admin
----------------

Works in concert with the Django ORM to provide automatic CRUD functionality

.. class:: incremental

You write the models, it provides the UI

.. class:: incremental center

You've seen this in action. Pretty neat, eh?


The Pareto Principle
--------------------

The Django Admin is a great example of the Pareto Priciple, a.k.a. the 80/20
rule:

.. class:: incremental center

**80% of the problems can be solved by 20% of the effort**

.. class:: incremental

The converse also holds true:

.. class:: incremental center

**Fixing the last 20% of the problems will take the remaining 80% of the
effort.**


Other Django Advantages
-----------------------

Clearly the most popular full-stack Python web framework at this time

.. class:: incremental

Popularity translates into:

.. class:: incremental

* Active, present community
* Plethora of good examples to be found online
* Rich ecosystem of *apps* (encapsulated add-on functionality)

.. class:: incremental center

**Jobs**


Active Development
------------------

Django releases in the last 12+ months (a short list):

.. class:: incremental

* 1.6.2 (February 2014)
* 1.6.1 (December 2013)
* 1.6 (November 2013)
* 1.4.10 (Novermber 2013)
* 1.5.5 (October 2013)
* 1.5 (February 2013)
* 1.4 (March 2012)


Great Documentation
-------------------

Thorough, readable, and discoverable.

.. class:: incremental

Led the way to better documentation for all Python

.. class:: incremental

`Read The Docs <https://readthedocs.org/>`_ - built in connection with
Django, sponsored by the Django Software Foundation.

.. class:: incremental

Write documentation as part of your python package, and render new versions of
that documentation for every commit

.. class:: incremental center

**this is awesome**


Where We Stand
--------------

For your homework this week, you created a ``Post`` model to serve as the heart
of our blogging app.

.. class:: incremental

You also took some time to get familiar with the basic workings of the Django
ORM.

.. class:: incremental

You made a minor modification to our model class and wrote a test for it.

.. class:: incremental

And you installed the Django Admin site and added your app to it.


Going Further
-------------

One of the most common features in a blog is the ability to categorize posts.

.. class:: incremental

Let's add this feature to our blog!

..  class:: incremental

To do so, we'll be adding a new model, and making some changes to existing code.

.. class:: incremental

This means that we'll need to *change our database schema*.


Changing a Database
-------------------

You've seen how to add new tables to a database using the ``syncdb`` command.

.. class:: incremental

The ``syncdb`` management command only creates tables that *do not yet exist*.
It **does not update tables**.

.. class:: incremental

The ``sqlclear <appname>`` command will print the ``DROP TABLE`` statements to
remove the tables for your app.

.. class:: incremental

Or ``sql <appname>`` will show the ``CREATE TABLE`` statements, and you can work
out the differences and update manually.

ACK!!!
------

That doesn't sound very nice, does it?

.. class:: incremental

Luckily, there is an app available for Django that helps with this: ``South``

.. class:: incremental

South allows you to incrementally update your database in a simplified way.

.. class:: incremental

South supports forward, backward and data migrations.

.. class:: incremental


Adding South
------------

South is so useful, that in Django 1.7 it will become part of the core
distribution of Django.

.. class:: incremental

But now it is not.  We need to add it, and set up our project to use it.

.. class:: incremental

Activate your django virtualenv and install South:

.. code-block:: bash

    $ source djagnoenv/bin/activate
    (djangoenv)$ pip install south
    ...
    Successfully installed south
    Cleaning up...


Installing South
----------------

Like other Django apps, South provides models of its own.  We need to enable them.

.. container:: incremental

    First, add ``south`` to your list of installed apps in ``settings.py``:

    .. code-block:: python
    
        INSTALLED_APPS = (
            ...
            'south', #< -add this line
            'myblog',
        )


Setting Up South
----------------

Then, run ``syncdb`` to pick up the tables it provides:

.. code-block:: bash

    (djangoenv)$ python manage.py syncdb
    Syncing...
    Creating tables ...
    Creating table south_migrationhistory
    ...

    Synced:
     ...
     > south
     > myblog

    Not synced (use migrations):
     -
    (use ./manage.py migrate to migrate these)


Hang On, What Just Happened?
----------------------------

You might have noticed that the output from ``syncdb`` looks a bit different
this time.

.. class:: incremental

This is because Django apps that use South do not use the normal ``syncdb``
command to initialize their SQL.

.. class:: incremental

Instead they use a new command that South provides: ``migrate``.

.. class:: incremental

This command ensures that only incremental changes are made, rather than
creating all of the SQL for an app every time.


Adding South to an App
----------------------

If you notice, our ``myblog`` app is still in the ``sync`` list. We need to add
South to it.

.. class:: incremental

Adding South to an existing Django project is quite simple. The trick is to do
it **before** you make any new changes to your models.

.. container:: incremental

    Simply use the ``convert_to_south`` management command, providing the name of
    your app as an argument:

    .. code-block:: bash

        (djangoenv)$ python manage.py convert_to_south myblog
        ...


What You Get
------------

After running this command, South will automatically create a first migration
for you that sets up tables looking exactly like what your app has now::

    myblog/
    ├── __init__.py
    ...
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0001_initial.pyc
    │   ├── __init__.py
    │   └── __init__.pyc
    ├── models.py
    ...

.. class:: incremental

South also automatically applies this first migration using the ``--fake``
argument, since the database is already in the proposed state.


Adding a Model
--------------

We want to add a new model to represent the categories our blog posts might
fall into.

.. class:: incremental

This model will need to have a name for the category, a longer description and
will need to be related to the Post model.

.. code-block:: python
    :class: small

    # in models.py
    class Category(models.Model):
        name = models.CharField(max_length=128)
        description = models.TextField(blank=True)
        posts = models.ManyToManyField(Post, blank=True, null=True,
                                       related_name='categories')


Strange Relationships
---------------------

In our ``Post`` model, we used a ``ForeignKeyField`` field to match an author
to her posts.

.. class:: incremental

This models the situatin in which a single author can have many posts, while
each post has only one author.

.. class:: incremental

But any given ``Post`` might belong in more than one ``Category``.

.. class:: incremental

And it would be a waste to allow only one ``Post`` for each ``Category``.

.. class:: incremental

Enter the ManyToManyField


Add a Migration
---------------

To get these changes set up, we now have to add a migration.

.. class:: incremental

We use the ``schemamigration`` management command to do so:

.. code-block:: bash

    (djangoenv)$ python manage.py schemamigration myblog --auto
     + Added model myblog.Category
     + Added M2M table for posts on myblog.Category
    Created 0002_auto__add_category.py. You can now apply this
    migration with: ./manage.py migrate myblog


Apply A Migration
-----------------

And south, along with making the migration, helpfully tells us what to do next:

.. code-block:: bash

    (djangoenv)$ python manage.py migrate myblog
    Running migrations for myblog:
     - Migrating forwards to 0002_auto__add_category.
     > myblog:0002_auto__add_category
     - Loading initial data for myblog.
    Installed 0 object(s) from 0 fixture(s)

.. class:: incremental

You can even look at the migration file you just applied,
``myblog/migrations/0002.py`` to see what happened.


Make Categories Look Nice
-------------------------

Let's make ``Category`` object look nice the same way we did with ``Post``.
Start with a test:

.. container:: incremental

    add this to ``tests.py``:

    .. code-block:: python
        :class: incremental
    
        # another import
        from myblog.models import Category
        
        # and the test case and test
        class CategoryTestCase(TestCase):

            def test_unicode(self):
                expected = "A Category"
                c1 = Category(name=expected)
                actual = unicode(c1)
                self.assertEqual(expected, actual)

Make it Pass
------------

Do you remember how you made that change for a ``Post``?

.. code-block:: python
    :class: incremental

    class Category(models.Model):
        #... 
        
        def __unicode__(self):
            return self.name


Admin for Categories
--------------------

Adding our new model to the Django admin is equally simple.

.. container:: incremental

    Simply add the following line to ``myblog/admin.py``

    .. code-block:: python

        # a new import
        from myblog.models import Category

        # and a new admin registration
        admin.site.register(Category)


Test It Out
-----------

Fire up the Django development server and see what you have in the admin:

.. code-block:: bash

    (djangoenv)$ python manage.py runserver
    Validating models...
    ...
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

.. class:: incremental

Point your browser at ``http://localhost:8000/admin/``, log in and play.

.. class:: incremental

Add a few categories, put some posts in them. Visit your posts, add new ones
and then categorize them.


A Public Face
-------------

Point your browser at http://localhost:8000/

.. class:: incremental

What do you see? 

.. class:: incremental

Why?

.. class:: incremental

We need to add some public pages for our blog.

.. class:: incremental

In Django, the code that builds a page that you can see is called a *view*.

Django Views
------------

A *view* can be defined as a *callable* that takes a request and returns a
response.

.. class:: incremental

This should sound pretty familiar to you.

.. class:: incremental

Classically, Django views were functions.

.. class:: incremental

Version 1.3 added support for Class-based Views (a class with a ``__call__``
method is a callable)


A Basic View
------------

Let's add a really simple view to our app.

.. class:: incremental

It will be a stub for our public UI.  Add this to ``views.py`` in ``myblog``

.. code-block:: python
    :class: small incremental

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


Hooking It Up
-------------

In your homework tutorial, you learned about Django **urlconfs**

.. class:: incremental

We used our project urlconf to hook the Django admin into our project.

.. class:: incremental

We want to do the same thing for our new app.

.. class:: incremental

In general, an *app* that serves any sort of views should contain its own 
urlconf.

.. class:: incremental

The project urlconf should mainly *include* these where possible.


Adding A Urlconf
----------------

Create a new file ``urls.py`` inside the ``myblog`` app package.

.. container:: incremental

    Open it in your editor and add the following code:

    .. code-block:: python
        :class: small
    
        from django.conf.urls import patterns, url

        urlpatterns = patterns('myblog.views',
            url(r'^$',
                'stub_view',
                name="blog_index"),
        )


A Word On Prefixes
------------------

The ``patterns`` function takes a first argument called the *prefix*

.. class:: incremental

When it is not empty, it is added to any view names in ``url()`` calls in the
same ``patterns``.

.. class:: incremental

In a root urlconf like the one in ``mysite``, this isn't too useful

.. class:: incremental

But in ``myblog.urls`` it lets us refer to views by simple function name

.. class:: incremental

No need to import every view.


Include Blog Urls
-----------------

In order for our new urls to load, we'll need to include them in our project
urlconf

.. container:: incremental

    Open ``urls.py`` from the ``mysite`` project package and add this:

    .. code-block:: python
        :class: small
    
        urlpatterns = patterns('',
            url(r'^', include('myblog.urls')), #<- add this
            #... other included urls
        )

.. class:: incremental

Try reloading http://localhost:8000/

.. class:: incremental

You should see some output now.


Project URL Space
-----------------

A project is defined by the urls a user can visit.

.. class:: incremental

What should our users be able to see when they visit our blog?

.. class:: incremental

* A list view that shows blog posts, most recent first.
* An individual post view, showing a single post (a permalink).

.. class:: incremental

Let's add urls for each of these, use the stub view for now.


Our URLs
--------

We've already got a good url for the list page: ``blog_index`` at '/'

.. container:: incremental

    For the view of a single post, we'll need to capture the id of the post.
    Add this to ``urlpatterns`` in ``myblog/urls.py``:
    
    .. code-block:: python 
        :class: small incremental
    
        url(r'^posts/(\d+)/$', 
            'stub_view', 
            name="blog_detail"),

.. class:: incremental

``(\d+)`` captures one or more digits as the post_id.

.. class:: incremental

Load http://localhost:8000/posts/1234/ and see what you get.


A Word on Capture in URLs
-------------------------

When you load the above url, you should see ``1234`` listed as an *arg*

.. container:: incremental

    Try changing the route like so:

    .. code-block:: python
        :class: small
    
        r'^posts/(?P<post_id>\d+)/$'

.. class:: incremental

Reload the same url. Notice the change.


Regular Expression URLS
-----------------------

Django, unlike Flask, uses Python regular expressions to build routes.

.. class:: incremental

When we built our WSGI book app, we did too.

.. class:: incremental

There we learned about regular expression *capture groups*. We just changed an
unnamed group to a named one.

.. class:: incremental

How you declare a capture group in your url pattern regexp influences how it
will be passed to the view callable.


Full Urlconf
------------

.. code-block:: python
    :class: small

    from django.conf.urls import patterns, url

    urlpatterns = patterns('myblog.views',
        url(r'^$',
            'stub_view',
            name="blog_index"),
        url(r'^posts/(?P<post_id>\d+)/$',
            'stub_view',
            name="blog_detail"),
    )


Testing Views
-------------

Before we begin writin real views, we need to add some tests for the views we
are about to create.

.. class:: incremental

We'll need tests for a list view and a detail view

.. container:: incremental

    add the following *imports* at the top of ``myblog/tests.py``:

    .. code-block:: python
    
        import datetime
        from django.utils.timezone import utc


Add a Test Case
---------------

.. code-block:: python
    :class: small

    class FrontEndTestCase(TestCase):
        """test views provided in the front-end"""
        fixtures = ['myblog_test_fixture.json', ]

        def setUp(self):
            self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
            self.timedelta = datetime.timedelta(15)
            author = User.objects.get(pk=1)
            for count in range(1,11):
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

.. class:: incremental

But in this blog, we have the ability to publish posts.

.. class:: incremental

Unpublished posts should not be seen in the front-end views.

.. class:: incremental

We set up our tests to have 5 published, and 5 unpublished posts

.. class:: incremental

Let's add a test to demonstrate that the right ones show up.


Testing the List View
---------------------

.. code-block:: python

        Class FrontEndTestCase(TestCase): # already here
        # ...
        def test_list_only_published(self):
            resp = self.client.get('/')
            self.assertTrue("Recent Posts" in resp.content)
            for count in range(1,11):
                title = "Post %d Title" % count
                if count < 6:
                    self.assertContains(resp, title, count=1)
                else:
                    self.assertNotContains(resp, title)

.. class:: incremental

Note that we also test to ensure that the unpublished posts are *not* visible.


Run Your Tests
--------------

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


Now Fix That Test!
------------------

Add the view for listing blog posts to ``views.py``.
    
.. code-block:: python
    :class: small

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


Getting Posts
-------------

.. code-block:: python
    :class: small

    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')

.. class:: incremental

We begin by using the QuerySet API to fetch all the posts that have
``published_date`` set

.. class:: incremental

Using the chaining nature of the API we order these posts by
``published_date``

.. class:: incremental

Remember, at this point, no query has actually been issued to the database.


Getting a Template
------------------

.. code-block:: python
    :class: small

    template = loader.get_template('list.html')

.. class:: incremental

Django uses configuration to determine how to find templates.

.. class:: incremental

By default, Django looks in installed *apps* for a ``templates`` directory

.. class:: incremental

It also provides a place to list specific directories.

.. class:: incremental

Let's set that up in ``settings.py``


Project Templates
-----------------

In ``settings.py`` add ``TEMPLATE_DIRS`` and add the absolute path to your 
``mysite`` project package:

.. code-block:: python
    :class: small
    
    TEMPLATE_DIRS = ('/absolute/path/to/mysite/mysite/templates', )

.. class:: incremental

Then add a ``templates`` directory to your ``mysite`` project package

.. class:: incremental

Finally, in that directory add a new file ``base.html`` and populate it with
the following:


base.html
---------

.. code-block:: jinja
    :class: small
    
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

.. class:: incremental

We've seen Jinja2 which was "inspired by Django's templating system".

.. class:: incremental

Basically, you already know how to write Django templates.

.. class:: incremental

Django templates **do not** allow any python expressions.

.. class:: incremental center small

https://docs.djangoproject.com/en/1.5/ref/templates/builtins/


Blog Templates
--------------

Our view tries to load ``list.html``.

.. class:: incremental

This template is probably specific to the blog functionality of our site

.. class:: incremental

It is common to keep shared templates in your project directory and
specialized ones in app directories.

.. class:: incremental 

Add a ``templates`` directory to your ``myblog`` app, too.

.. class:: incremental

In it, create a new file ``list.html`` and add this:


list.html
---------

.. code-block:: jinja
    :class: tiny
    
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


Template Context
----------------

.. code-block:: python
    :class: small

    context = RequestContext(request, {
        'posts': posts,
    })
    body = template.render(context)

.. class:: incremental

Like Jinja2, django templates are rendered by passing in a *context*

.. class:: incremental

Django's RequestContext provides common bits, similar to the global context in
Flask

.. class:: incremental

We add our posts to that context so they can be used by the template.


Return a Response
-----------------

.. code-block:: python
    :class: small

    return HttpResponse(body, content_type="text/html")

.. class:: incremental

Finally, we build an HttpResponse and return it.

.. class:: incremental

This is, fundamentally, no different from the ``stub_view`` just above.


Fix URLs
--------

We need to fix the url for our blog index page

.. container:: incremental

    Update ``urls.py`` in ``myblog``:

    .. code-block:: python
        :class: small
    
        url(r'^$',
            'list_view',
            name="blog_index"),

.. class:: incremental small

::

    (djangoenv)$ python manage.py test myblog
    ...
    Ran 3 tests in 0.033s

    OK


Common Patterns
---------------

This is a common pattern in Django views:

.. class:: incremental

* get a template from the loader
* build a context, usually using a RequestContext
* render the template
* return an HttpResponse

.. class:: incremental

So common in fact that Django provides two shortcuts for us to use:

.. class:: incremental

* ``render(request, template[, ctx][, ctx_instance])``
* ``render_to_response(template[, ctx][, ctx_instance])``


Shorten Our View
----------------

Let's replace most of our view with the ``render`` shortcut

.. code-block:: python
    :class: small

    from django.shortcuts import render # <- already there
    
    # rewrite our view
    def list_view(request):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        context = {'posts': posts}
        return render(request, 'list.html', context)

.. class:: incremental

Remember though, all we did manually before is still happening


Our Detail View
---------------

Next, let's add a view function for the detail view of a post

.. class:: incremental

It will need to get the ``id`` of the post to show as an argument

.. class:: incremental

Like the list view, it should only show published posts

.. class:: incremental

But unlike the list view, it will need to return *something* if an unpublished
post is requested.

.. class:: incremental

Let's start with the tests in ``views.py``


Testing the Details
-------------------

Add the following test to our ``FrontEndTestCase`` in ``myblog/tests.py``:

.. code-block:: python
    :class: small incremental

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


Run Your Tests
--------------

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


Let's Fix That Test
-------------------

Now, add a new view to ``myblog/views.py``:

.. code-block:: python
    :class: incremental small

    def detail_view(request, post_id):
        published = Post.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        context = {'post': post}
        return render(request, 'detail.html', context)


Missing Content
---------------

One of the features of the Django ORM is that all models raise a DoesNotExist
exception if ``get`` returns nothing.

.. class:: incremental

This exception is actually an attribute of the Model you look for. There's also
an ``ObjectDoesNotExist`` for when you don't know which model you have.

.. class:: incremental

We can use that fact to raise a Not Found exception.

.. class:: incremental

Django will handle the rest for us.


Add the Template
----------------

We also need to add ``detail.html`` to ``myblog/templates``:

.. code-block:: jinja
    :class: tiny

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


Hook it Up
----------

In order to view a single post, we'll need a link from the list view

.. container:: incremental

    We can use the ``url`` template tag (like flask ``url_for``):

    .. code-block:: jinja
        :class: small
    
        {% url '<view_name>' arg1 arg2 %}

.. class:: incremental

In our ``list.html`` template, let's link the post titles:

.. code-block:: jinja
    :class: small incremental

    {% for post in posts %}
    <div class="post">
      <h2>
        <a href="{% url 'blog_detail' post.pk %}">{{ post }}</a>
      </h2>
      ...


Fix URLs
--------

Again, we need to insert our new view into the existing ``myblog/urls.py`` in
``myblog``:

.. code-block:: python
    :class: small
    
    url(r'^posts/(?P<post_id>\d+)/$',
        'detail_view',
        name="blog_detail"),

.. class:: incremental small

::

    (djangoenv)$ python manage.py test myblog
    ...
    Ran 4 tests in 0.077s

    OK


A Moment To Play
----------------

We've got some good stuff to look at now.  Fire up the server

.. class:: incremental

Reload your blog index page and click around a bit.

.. class:: incremental

You can now move back and forth between list and detail view.

.. class:: incremental

Try loading the detail view for a post that doesn't exist


Congratulations
---------------

You've got a functional Blog

.. class:: incremental

It's not very pretty, though.

.. class:: incremental

We can fix that by adding some css

.. class:: incremental

This gives us a chance to learn about Django's handling of *static files*


Static Files
------------

Like templates, Django expects to find static files in particular locations

.. class:: incremental

It will look for them in a directory named ``static`` in any installed apps.

.. class:: incremental

They will be served from the url path in the STATIC_URL setting.

.. class:: incremental

By default, this is ``/static/``


Add CSS
-------

I've prepared a css file for us to use. You can find it in the class resources

.. class:: incremental

Create a new directory ``static`` in the ``myblog`` app.

.. class:: incremental

Copy the ``django_blog.css`` file into that new directory.

.. container:: incremental

    Then add this link to the <head> of ``base.html``:

    .. code-block:: html
        :class: small
    
        <title>My Django Blog</title>
        <link type="text/css" rel="stylesheet" href="/static/django_blog.css">


View Your Results
-----------------

Reload http://localhost:8000/ and view the results of your work

.. class:: incremental

We now have a reasonable view of the posts of our blog on the front end

.. class:: incremental

And we have a way to create and categorize posts using the admin

.. class:: incremental

However, we lack a way to move between the two.

.. class:: incremental

Let's add that ability next.


Adding A Control Bar
--------------------

We'll start by adding a control bar to our ``base.html`` template:

.. code-block:: jinja
    :class: small

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


Request Context Revisited
-------------------------

When we set up our views, we used the ``render`` shortcut, which provides a
``RequestContext``

.. class:: incremental

This gives us access to ``user`` in our templates

.. class:: incremental

It provides access to methods about the state and rights of that user

.. class:: incremental

We can use these to conditionally display links or UI elements. Like only
showing the admin link to staff members.


Login/Logout
------------

Django also provides a reasonable set of views for login/logout.

.. class:: incremental

The first step to using them is to hook them into a urlconf.

.. container:: incremental

    Add the following to ``mysite/urls.py``:
    
    .. code-block:: python
        :class: small
    
        url(r'^', include('myblog.urls')), #<- already there
        url(r'^login/$',
            'django.contrib.auth.views.login',
            {'template_name': 'login.html'},
            name="login"),
        url(r'^logout/$',
            'django.contrib.auth.views.logout',
            {'next_page': '/'},
            name="logout"),


Login Template
--------------

We need to create a new ``login.html`` template in ``mysite/templates``:

.. code-block:: jinja
    :class: small

    {% extends "base.html" %}

    {% block content %}
    <h1>My Blog Login</h1>
    <form action="" method="POST">{% csrf_token %}
      {{ form.as_p }}
      <p><input type="submit" value="Log In"></p>
    </form>
    {% endblock %}


Submitting Forms
----------------

In a web application, submitting forms is potentially hazardous

.. class:: incremental

Data is being sent to our application from some remote place

.. class:: incremental

If that data is going to alter the state of our application, we **must** use 
POST

.. class:: incremental

Even so, we are vulnerable to Cross-Site Request Forgery, a common attack
vector.


Danger: CSRF
------------

Django provides a convenient system to fight this.

.. class:: incremental

In fact, for POST requests, it *requires* that you use it.

.. class:: incremental

The Django middleware that does this is enabled by default. 

.. class:: incremental

All you need to do is include the ``{% csrf_token %}`` tag in your form.


Hooking It Up
-------------

In ``base.html`` make the following updates:

.. code-block:: jinja
    :class: small

    <!-- admin link -->
    <a href="{% url 'admin:index' %}">admin</a>
    <!-- logout link -->
    <a href="{% url 'logout' %}">logout</a>
    <!-- login link -->
    <a href="{% url 'login' %}">login</a>

.. container:: incremental

    Finally, in ``settings.py`` add the following:

    .. code-block:: python
        :class: small
    
        LOGIN_URL = '/login/'
        LOGIN_REDIRECT_URL = '/'


Forms In Django
---------------

In adding a login view, we've gotten a sneak peak at how forms work in Django.

.. class:: incremental

However, learning more about them is beyond what we can achieve in this
session.

.. class:: incremental

The form system in Django is quite nice, however. I urge you to `read more about it`_ 

.. _read more about it: https://docs.djangoproject.com/en/1.6/topics/forms/

.. class:: incremental

In particular, you might want to pay attention to the documentation on `Model Forms`

.. _Model Forms: https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/


Ta-Daaaaaa!
-----------

So, that's it.  We've created a workable, simple blog app in Django.

.. class:: incremental

There's much more we could do with this app. And for homework, you'll do some
of it.

.. class:: incremental

Then next session, we'll work as we did in session 6.

..  class:: incremental

We'll divide up into pairs, and implement a simple feature to extend our blog.


Homework
--------

For your homework this week, we'll fix one glaring problem with our blog admin.

.. class:: incremental

As you created new categories and posts, and related them to each-other, how
did you feel about that work?

.. class:: incremental

Although from a data perspective, the category model is the right place for the
ManytoMany relationship to posts, this leads to awkward usage in the admin.

.. class:: incremental

It would be much easier if we could designate a category for a post *from the
Post admin*.


Your Assignment
---------------

You'll be reversing that relationship so that you can only add categories to posts

Take the following steps:

1. Read the documentation about the `Django admin.`_
2. You'll need to create a customized `ModelAdmin`_ class for the ``Post`` and
   ``Category`` models.
3. And you'll need to create an `InlineModelAdmin`_ to represent Categories on
   the Post admin view.
4. Finally, you'll need to `suppress the display`_  of the 'posts' field on
   your ``Category`` admin view.


.. _Django admin.: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/
.. _ModelAdmin: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#modeladmin-objects
.. _InlineModelAdmin: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#inlinemodeladmin-objects
.. _suppress the display: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#modeladmin-options


Pushing Further
---------------

All told, those changes should not require more than about 15 total lines of
code.

The trick of course is reading and finding out which fifteen lines to write.

If you complete that task in less than 3-4 hours of work, consider looking into
other ways of customizing the admin.


Tasks you might consider
------------------------

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
