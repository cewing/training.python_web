Internet Programming with Python
================================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Session 8: A Django Application

.. class:: intro-blurb right

Wherein we complete our Django blog app.

.. class:: image-credit

image: http://djangopony.com/


Where We Stand
--------------

We've created a couple of models, Post and Category, that make up our blog
app.

.. class:: incremental

We've taken some time to get familiar with the basic workings of the Django
ORM.

.. class:: incremental

We've made a minor modification to our model classes and written tests for it.

.. class:: incremental

And we've installed the Django Admin site and added our app to it.


Customizing the Admin
---------------------

We have noted, however, that the admin isn't exactly right for our needs.

.. class:: incremental

* Listing of posts should show created, modified and published dates
* Listing of posts should show the author of a post, with a link to the author
* The date information for a post should be displayed on the edit page
* It should be possible to add a post to a category while creating or editing
  it

.. class:: incremental small center

https://docs.djangoproject.com/en/1.5/ref/contrib/admin/


The ModelAdmin Class
--------------------

Open ``admin.py`` from your ``myblog`` package.

.. class:: incremental

* The ``admin.site`` is a globally available instance of the ``Admin`` class.
* It is initialized at runtime automatically.
* It stores a registry of the models that are registered with it.
* Each call to ``admin.site.register`` adds a new model to the global *site*.
* ``register`` takes two args: a *Model* subclass and an optional *ModelAdmin* subclass
* If you call it without the optional subclass, you get the default.

.. class:: incremental

Most usable admin functions are provided by the ModelAdmin.


Custom ModelAdmin
-----------------

Our first task is to list date and author information.

.. container:: incremental

    In ``admin.py`` add the following code ():

    .. code-block:: python
        :class: small

        # this is new
        class PostAdmin(admin.ModelAdmin):
            list_display = ('__unicode__', 'created_date', 'modified_date',
                            'published_date', 'author')
    
        admin.site.register(Post, PostAdmin) #<- update this registration

.. class:: incremental

Let's see what that did.


View The Results
----------------

If you haven't already, activate your virtualenv then fire up the development
server:

::

    (djangoenv)$ python manage.py runserver

.. class:: incremental

Load http://localhost:8000/admin and click through to the Post admin.

.. class:: incremental

Pretty simple, eh?


List Display
------------

A Couple of things about the ``list_display`` option are important to know:

.. class:: incremental

* The value you provide must be an iterable even if it has only one item 
* Each item in the iterable becomes a column in the list 
* The first item is the one that links to the change page for that object
  
  * That can be customized by the ``list_display_links`` option 
  
* Listed items can be field names or callables.

* Callables can be module-level functions, or methods on the ModelAdmin or
  Model


A Better Author Listing
-----------------------

Let's use this last bit to fix the author listing.

.. class:: incremental

We'll need functionality that provides:

.. class:: incremental

* The full name of the author, if present, otherwise the username.
* A link to the admin change form for that author.

.. class:: incremental

Where should this go? Module? ModelAdmin? Model?

.. class:: incremental

* The first could be useful in public listings
* The second is really only useful on the backend


Add Tests
---------

In ``tests.py`` add the following test:

.. code-block:: python
    :class: small
    
    class PostTestCase(TestCase):
        #...
        def test_author_name(self):
            for author in User.objects.all():
                fn, ln, un = (author.first_name, 
                              author.last_name,
                              author.username)
                author_name = Post(author=author).author_name()
                if not (fn and ln):
                    self.assertEqual(author_name, un)
                else:
                    if fn:
                        self.assertTrue(fn in author_name)
                    if ln:
                        self.assertTrue(ln in author_name)


Add Tests
---------

To test the admin, we'll first need a new TestClass:

.. code-block:: python
    :class: small

    # new imports
    from django.contrib.admin.sites import AdminSite
    from myblog.admin import PostAdmin

    # new TestCase
    class PostAdminTestCase(TestCase):
        fixtures = ['myblog_test_fixture.json', ]

        def setUp(self):
            admin = AdminSite()
            self.ma = PostAdmin(Post, admin)
            for author in User.objects.all():
                title = "%s's title" % author.username
                post = Post(title=title, author=author)
                post.save()


Add Tests
---------

And then we need a test added to it:

.. code-block:: python
    :class: small

    def test_author_link(self):
        expected_link_path = '/admin/auth/user/%s'
        for post in Post.objects.all():
            expected = expected_link_path % post.author.pk
            actual = self.ma.author_link(post)
            self.assertTrue(expected in actual)

.. container:: incremental

    Quit the django server and run your tests:
    
    .. class:: small
    
    ::
    
        (djangoenv)$ python manage.py test myblog
        ...
        Ran 4 tests in 0.026s
        FAILED (errors=2)


Make Them Pass
--------------

First, add the ``author_name`` method to our Post model in ``models.py``:

.. code-block:: python
    :class: small

    def author_name(self):
        raw_name = "%s %s" % (self.author.first_name,
                              self.author.last_name)
        name = raw_name.strip()
        if not name:
            name = self.author.username
        return name

.. class:: small incremental

::

    (djangoenv)$ python manage.py test myblog
    ...
    Ran 4 tests in 0.027s
    FAILED (errors=1)


Make Them Pass
--------------

Finally, add the ``author_link`` method to the PostAdmin in ``admin.py``:

.. code-block:: python
    :class: small

    # add an import
    from django.core.urlresolvers import reverse

    # and a method
    class PostAdmin(admin.ModelAdmin):
        #...
        def author_link(self, post):
            url = reverse('admin:auth_user_change', args=(post.id,))
            name = post.author_name()
            return '<a href="%s">%s</a>' % (url, name)

.. class:: small incremental

::

    (djangoenv)$ python manage.py test myblog
    ...Ran 4 tests in 0.035s
    OK


Hook It Up
----------

First, replace the ``'author'`` name in ``list_display`` with
``'author_link'``:

.. code-block:: python
    :class: small
    
    list_display = (..., 'author_link')

.. container:: incremental

    We also need to let the admin know our HTML is safe:

    .. code-block:: python
        :class: small

        def author_link(self, post):
            #... method body
        author_link.allow_tags = True


Wait, What??
------------

In Python, *everything* is an object. Even methods of classes.

.. class:: incremental

The Django admin uses special *method attributes* to control the methods you 
create for ``list_display``.

.. container:: incremental

    Another special attribute controls the column title used in the list page:

    .. code-block:: python
        :class: small
        
        def author_link(self, post):
            #... method body
        author_link.allow_tags = True
        author_link.short_description = "Author" #<- add this


See The Results
---------------

Start up the Django server again and see what you've done:

.. class:: small

::

    (djangoenv)$ python manage.py runserver

.. class:: incremental

Reload your admin site, click on the Post admin and see the new 'Author'
column.

.. class:: incremental

* Click on an author name.
* Set the first and last names (if you haven't already).
* Go back to Posts and see the outcome of this change.

.. class:: incremental

Not bad, eh?


Change Form Fields
------------------

Date fields that have ``auto_now`` or ``auto_now_add`` set automatically 
become uneditable.

.. class:: incremental

Because they are uneditable, the Django Admin leaves them out.

.. class:: incremental

We'd like to see them, though.

.. class:: incremental

We can use another built-in Admin option to help us: ``readonly_fields``


Update PostAdmin
----------------

Again, in ``admin.py`` let's add the following to our PostAdmin class:

.. code-block:: python
    :class: small

    class PostAdmin(admin.ModelAdmin):
        list_display = (...)
        readonly_fields = ('created_date', 'modified_date')
        #...

.. class:: incremental

Reload the Admin and click on a single post.  Did that work?

.. class:: incremental

Add a new post and look at the form.  How do those fields look?


Hide Fields on Add
------------------

Our readonly fields really shouldn't be there when we add a new object.

.. class:: incremental

ModelAdmin provides a hook to customize this: ``get_readonly_fields``.

.. class:: incremental

Overriding this is altering standard functionality, so let's add a test
proving:

.. class:: incremental

* If we load the form to add a post, we don't see these fields
* If we load the form to edit a post, we do.


Add A Test
----------

In our PostAdminTestCase class, add:

.. code-block:: python
    :class: small
    
    # add this to the setUp() method:
    def setUp(self):
        #...
        self.client.login(username='admin', password='secret')

    # and add a new test method:
    def test_readonly_fields_in_page(self):
        readonly_fields = self.ma.readonly_fields
        add_resp = self.client.get('/admin/myblog/post/add/')
        for fieldname in readonly_fields:
            self.assertFalse(fieldname in add_resp.content)
        for post in Post.objects.all():
            edit_resp = self.client.get('/admin/myblog/post/%d/' % post.pk)
            for fieldname in readonly_fields:
                self.assertTrue(fieldname in edit_resp.content)


Run The Test
------------

We're using the test client. Django provides this automatically on TestCase
subclasses.

.. container:: incremental

    Quit the django browser and run your tests:

    .. class:: small
    
    :: 
    
        (djangoenv)$ python manage.py test myblog
        ...
        ----------------------------------------------------------------------
        Ran 5 tests in 0.302s

        FAILED (failures=1)


Make It Pass
------------

.. container:: incremental

    Override ``get_readonly_fields`` on the PostAdmin class:
    
    .. code-block:: python
        :class: small incremental

        def get_readonly_fields(self, request, obj=None):
            fields = ()
            # if there is no object, we must be adding a new post
            # otherwise we are editing one that exists.
            if obj is not None:
                fields = self.readonly_fields
            return fields

.. class:: incremental small

::

    (djangoenv)$ python manage.py test myblog
    ...
    Ran 5 tests in 0.364s
    OK


Categorize Posts
----------------

We'd like to be able to add categories to posts while adding or editing them.

.. class:: incremental

But there is no field on the ``Post`` model that would show them.

.. class:: incremental

Django provides the concept of an ``inline`` form to allow adding objects that
are related when there is no field available.

.. class:: incremental

In the Django Admin, these are created using subclasses of the
``InlineAdmin``.


Create an Inline Admin
----------------------

In ``admin.py`` add the following code *above* the definition of PostAdmin:

.. code-block:: python
    :class: small

    class CategoryInlineAdmin(admin.TabularInline):
        model = Category.posts.through
        extra = 1

.. container:: incremental

    And then add one line to the PostAdmin class definition:

    .. code-block:: python
        :class: small
    
        class PostAdmin(admin.ModelAdmin):
            #... other options
            inlines = [CategoryInlineAdmin, ]
            
            #... methods

Try It Out
----------

Restart the Django server and see what you've done:

.. class:: small

::

    (djangoenv)$ python manage.py runserver

.. class:: incremental

Note that you can even add *new* categories via the inline form.

.. class:: incremental

But, in the form for a category, you see the field for Post. That shouldn't be
there.


A Final Tweak
-------------

See if you can figure out how to remove the ``posts`` field from the
CategoryAdmin.

.. code-block:: python
    :class: small incremental
    
    # create a custom model admin class
    class CategoryAdmin(admin.ModelAdmin):
        exclude = ('posts', )
    
    # and register Category to use it in the Admin
    admin.site.register(Category, CategoryAdmin)


PLACEHOLDER
-----------

Do we have time to do an admin action here? if so, add actions to publish,
unpublish items in bulk


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

    from django.http import HttpResponse

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

We talked in the previous session about the Django urlconf

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


Project URL Space
-----------------

A project is defined by the urls a user can visit.

.. class:: incremental

What should our users be able to see when they visit our blog?

.. class:: incremental

* A list view that shows blog posts, most recent first.
* An individual post view, showing a single post (a permalink).
* An archive view that shows all posts for a year, or a month within a year.
* A category view that shows all posts in a given category.

.. class:: incremental

Let's add urls for each of these, use the stub view for now.


Our URLs
--------

We've already got a good url for the list page: ``blog_index`` at '/'

.. container:: incremental

    For the view of a single post, we'll need to capture the id of the post.
    Add this to ``urlpatterns``:
    
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

    Try changing the regexp like so:

    .. code-block:: python
        :class: small
    
        r'^posts/(?P<post_id>\d+)/$'

.. class:: incremental

Reload the same url. Notice the change.

.. class:: incremental

How you declare a capture group in your url pattern regexp influenced how it
will be passed to the view callable.


Archive View URLs
-----------------

Consider our archive requirement.

.. container:: incremental

    Can you think of a way to use one view for that?
    
    .. code-block:: python
        :class: small incremental
    
        url(r'^archive/(?P<year>[\d]{4})/$',
            'stub_view', #<- this can be the same view
            name="yearly_archive"),
        url(r'^archive/(?P<year>[\d]{4})/(?P<month>[\d]{2})/$',
            'stub_view', #<- in multiple urls
            name="monthly_archive"),

.. class:: incremental

In this case, month is *optional*, so it **must** be a kwarg


