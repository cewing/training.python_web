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

Before we begin, we need to add some tests for the views we are about to 
create.

.. class:: incremental

We'll need tests for a list view and a detail view

.. class:: incremental

To save us time, I've written these tests already

.. class:: incremental

You can find them in the class resources directory: ``blog_view_tests.py``

.. class:: incremental

Copy the contents of that file into our blog ``tests.py`` file.


Run The Tests
-------------

::

    (djangoenv)$ python manage.py test myblog
    ...
    ----------------------------------------------------------------------
    Ran 7 tests in 0.478s

    FAILED (failures=2)
    Destroying test database for alias 'default'...


Our First View
--------------

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

In ``settings.py`` find ``TEMPLATE_DIRS`` and add the absolute path to your 
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
    Ran 7 tests in 0.494s
    FAILED (failures=1)


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

    # replace RequestContext and loader import
    from django.shortcuts import render
    
    # rewrite our view
    def list_view(request):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        context = {'posts': posts}
        return render(request, 'list.html', context)

.. class:: incremental

Remember though, all we did manually before is still happening


Detail View
-----------

Next, let's write a view function for the detail view of a post

.. container:: incremental

    It should have the following signature:

    .. code-block:: python
        :class: small
    
        detail_view(request, post_id)

.. class:: incremental

We will call the template ``detail.html``

.. class:: incremental

Let's start with the code in ``views.py``


detail_view
-----------

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

.. class:: incremental

All models raise a DoesNotExist exception if ``get`` returns nothing.

.. class:: incremental

We can use that fact to raise a Not Found exception.

.. class:: incremental

Django will handle the rest for us.


detail.html
-----------

.. code-block:: jinja
    :class: small
    
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

    We can use the ``url`` template tag (like flask url_for):

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

Again, we need to insert our new view into the existing ``urls.py`` in
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
    Ran 7 tests in 0.513s
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

Copy the ``django_css`` file into that new directory.

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
            {% if user.is_admin %}<li>admin</li>{% endif %}
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

We can use these to conditionally display links or UI elements.


Login/Logout
------------

Django provides a reasonable set of views for login/logout.

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


Handling Forms
--------------

Adding login and logout has given us a sneak peek at forms.

.. class:: incremental

But there is a *lot* of magic happening that we should see directly.

.. class:: incremental

As a last task, let's add a non-admin way to create new posts.

.. class:: incremental

We'll use a form, submit it to a view, and have it create a new Post object


Django Forms
------------

Forms are, like Models, a Django *class*

.. class:: incremental

Like Models, you add fields to a form as class *attributes*

.. class:: incremental

Like Model fields, the fields on a form are also Python class instances.

.. class:: incremental

Unlike Model fields, Form fields are built to interact with data in a
*request*

.. class:: incremental

By tradition, they are created in a module called ``forms.py``


Post Form
---------

Create ``forms.py`` in ``myblog`` and open it in your editor.

.. code-block:: python
    :class: small
    
    from django import forms
    from myblog.models import Post
    
    class PostForm(forms.ModelForm):
        
        class Meta:
            model = Post
            fields = ('title', 'text', 'author')

.. class:: incremental

The ``ModelForm`` class generates fields based on the model.

.. class:: incremental

Use ``fields`` to force only a subset of those.


A View for Our Form
-------------------

The basic approach to handling forms in Django always follows this pattern:

.. code-block:: python
    :class: small
    
    if request.method == 'POST':
        # bind a form instance to POST data
        if form.is_valid():
            # process the form data here
            # tell the user about the success
        else:
            # tell the user about the problem
    else:
        # create an unbound form
    # render the form template

.. class:: incremental

Let's create a ``add_post`` view that does this with our ``PostForm``

add_post view
-------------

.. code-block:: python
    :class: small 

    # add imports to views.py
    from django.core.exceptions import PermissionDenied
    from django.contrib import messages
    from django.core.urlresolvers import reverse
    from myblog.forms import PostForm
    
    # and a new view function:
    def add_view(request):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied
        if request.method == 'POST':
            form = PostForm(request.POST)
            # handle form submission
        else:
            form = PostForm()
        context = {'form': form}
        return render(request, 'add.html', context)


Add A URL
---------

In ``myblog/urls.py`` add a new entry to our urlconf:

.. code-block:: python
    :class: small
    
    url(r'^add/$',
        'add_view',
        name="add_post"),

.. container:: incremental

    And hook it up to the control bar link in ``base.html``

    .. code-block:: jinja
    
        <!-- update new post link -->
        <a href="{% url 'add_post' %}">new post</a>


Create add.html
---------------

Finally, we need to create a template, ``add.html`` in ``myblog/templates``:

.. code-block:: jinja
    :class: small
    
    {% extends "base.html" %}

    {% block content %}
    <h1>New Blog Post</h1>
    <form action="" method="POST">{% csrf_token %}
      {{ form.as_p }}
      <p><input type="submit" value="Save"></p>
    </form>
    {% endblock %}


Try it Out
----------

You should be able to click on the 'new post' button in the control bar.

.. class:: incremental

How does the form look?

.. class:: incremental

It would be nice if the 'author' field were auto-populated, and even hidden.

.. class:: incremental

Let's do that next.


Form 'initial'
--------------

When instantiating a form, you can pass it *initial* values.

.. container:: incremental

    In ``views.py`` make the following changes to the ``add_view``:

    .. code-block:: python
        :class: small
    
        def add_view(request):
            user = request.user
            if not user.is_authenticated:
                raise PermissionDenied
            if request.method == 'POST':
                #... not quite ready for this yet.
            else:
                initial = {'author': user} #<- add this
                form = PostForm(initial=initial) #<- updated


Hidden Fields
-------------

If you reload, you should now see ``author`` pre-popluated.

.. container:: incremental

    To hide it, we must update the 'widget' it will use in ``forms.py``:

    .. code-block:: python
        :class: small
    
        class PostForm(forms.ModelForm):

            class Meta:
                #...
                widgets = {
                    'author': forms.HiddenInput(),
                }

.. class:: incremental

Reload again to see the input disappear. Check page source to see the 'hidden'
input.


Form Submission
---------------

That's all we need to have for processing.  We want to:

.. class:: incremental

* Validate the form input
* Report validation errors to the user and return the bound form
* If no errors occur, save the form, creating an instance
* Report success to the user and redirect to the list homepage.

.. class:: incremental

Django's ``messages`` framework will allow notifications.


Handle a Submitted Form
-----------------------

In ``views.py``, update the ``add_view``:

.. code-block:: python
    :class: small
    
    def add_view(request):
        user = request.user
        if not user.is_authenticated():
            raise PermissionDenied
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
                msg = "post '%s' saved" % post
                messages.add_message(request, messages.INFO, msg)
                return HttpResponseRedirect(reverse('blog_index'))
            else:
                messages.add_message(request, messages.INFO, 
                                     "please fix the errors below")
        else:
            #...


Showing Messages
----------------

The ``messages`` framework pushes messages onto a stack.

.. class:: incremental

You can then pop them back off by printing them in a template.

.. container:: incremental

    In ``base.html`` let's give them a place to go:

    .. code-block:: jinja
        :class: small
    
        <div id="container">
          {% if messages %}
          <div class="notifications">
           {% for message in messages %}
           <p>{{ message }}</p>
           {% endfor %}
          </div>
          {% endif %}
          <!-- main content div below here -->


Final Run
---------

That should be enough to get us going.

.. class:: incremental

Fill out your form, supplying title and text.  

.. class:: incremental

Submit the form, and notice the messaging from the system.

.. class:: incremental

Why is your new post not appearing in the blog list?


Next Steps
----------

There are a number of improvements one could make to this blog system:

.. class:: incremental

* Send email notifications to "blog administrators" that would notify them of
  new posts awaiting publication.
* Provide a second list view giving users access to edit their unpublished
  posts.
* Provide restricted access to certain users to view all unpublished posts and
  choose to publish them.
* Add a form field for the post category and put the post in a category when
  processing the form
* Provide a list view of a category, showing all posts in it. 
* Provide HTML editing for post text.


That's All For Now
------------------

But this is all we have time for in this session.

.. class:: big-centered incremental

We'll see you next session!
