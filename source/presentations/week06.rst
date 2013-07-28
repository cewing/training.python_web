Internet Programming with Python
================================

blah blah blah






Django Views
------------

Django views are callables that take a request and return a response.

.. class:: incremental

From the beginning, these have been functions.  They still can be.

.. class:: incremental

Version 1.3 added support for Class-based Views.

.. class:: incremental

Really, they've always been there implicitly. The Admin is just a big
class-based view.

Generic Views
-------------

One of the most common uses for Class-based Views is in creating Generic Views.

.. class:: incremental

Some public views are so common that providing a simple and generic interface
for making them is a big win.

.. class:: incremental

* Showing a list of objects of some type.
* Showing the details of a single object of some type.
* Displaying a static HTML template (or a template with some dynamic context)
* Displaying and processing a simple HTML form.

Our Application
---------------

We'd like to be able to add some views that show our polls to the public.

.. class:: incremental

What views would we like to have?

.. class:: incremental

* A list of all polls, perhaps ordered by publication date
* A display of a single poll, showing each choice and allowing a vote
* A view that processes a vote
* A view that shows the poll results after you vote.

.. class:: incremental

I start by configuring my URLs, it helps me think about the app API.

Configure URLs
--------------

In your ``polls`` app package, add a new file: ``urls.py``. Open it in an
editor:

.. code-block:: python
    :class: incremental small
    
    from django.conf.urls import patterns, url
    from django.http import HttpResponse

    def stub(request, *args, **kwargs):
        return HttpResponse('stub view', mimetype="text/plain")

    urlpatterns = patterns('',
        url(r'^$', stub, name="poll_list"),
        url(r'^(?P<pk>\d+)/$', stub, name="poll_detail"),
        url(r'^(?P<pk>\d+)/vote/$' stub, name="poll_vote"),
        url(r'^(?P<pk>\d+)/result/$', stub, name="poll_result"),
    )

Hook URLs to the Root
---------------------

Like with the Django Admin, we can now add all the urls for our poll app at
once.

.. class:: incremental

In the ``urls.py`` in our ``mysite`` project package, add the following:

.. code-block:: python
    :class: incremental small

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^polls/', include('polls.urls')), # ADD
    )

.. class:: incremental

Restart the development server and load ``http://localhost:8000/polls/``

Generic Poll List
-----------------

Django's Generic Views allow you to do quite a lot with just a little code.
Edit ``urls.py``:

.. code-block:: python
    :class: incremental small

    # add this import
    from django.views.generic import ListView
    
    # edit the url pattern for the poll list:
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='polls',
            template_name="polls/list.html"
        ),
        name="poll_list"),

.. class:: incremental

Now, we just need to make that template

Django Templates
----------------

The `Django Template Language
<https://docs.djangoproject.com/en/1.4/topics/templates/>`_ looks a *lot* like
Jinja2. It is, however, quite a bit more limited.

.. class:: incremental

* variables available in context may be printed with ``{{ name }}``
* variables that are objects or dictionaries may be addressed with dots: ``{{
  name.attr }}``
* *filters* are available and look the same ``{{ name|upper }}``
* logical *tags*: ``{% for x in y %}{{ x }}{% endfor %}``
* available filters and tags may be extended with custom code
* templates can be *extended* and *included*
* you may define *blocks* in templates to be filled by other templates.
* you **may not** execute arbitrary python or assign variables and use them

Setting Up
----------

In ``assignments/week06/lab/source`` you'll find a file ``base.html``.

.. class:: incremental

Create a new directory, ``templates`` in your ``polls`` app package.

.. class:: incremental

Copy the ``base.html`` file into that new directory.

.. class:: incremental

Next, create a folder ``polls`` *inside* that new templates directory. We'll
add our individual templates here.

List Template
-------------

Add ``list.html`` inside ``templates/polls``:

.. code-block:: django
    :class: small

    {% extends "base.html" %}

    {% block content %}
    <h1>Latest Polls</h1>
    {% for poll in polls %}
    <div class="poll">
      <h2><a href="{% url poll_detail poll.pk %}">{{ poll }}</a></h2>
    </div>
    {% endfor %}
    {% endblock %}

.. class:: incremental

Now, load ``http://localhost:8000/polls/`` again.  

Detail View
-----------

Back in our ``polls`` app, let's edit ``urls.py`` again:

.. code-block:: python
    :class: incremental small

    # add this import
    from django.views.generic import ListView
    
    # and edit the detail url like so:
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/detail.html"
        ),
        name="poll_detail"),

.. class:: incremental

Again, we only need to add a template.

Forms in Django
---------------

We want to be able to vote on a poll. 

.. class:: incremental

Because doing so involves changing data on the server, we should do this with
a POST request.

.. class:: incremental

An html form is a simple way to allow us to force a POST request.

.. class:: incremental

Data-altering requests are vulnerable to Cross-Site Request Forgery, a common
attack vector.

Danger: CSRF
------------

Django not only provides a convenient system to fight this, it *requires* it
for any POST requests.

.. class:: incremental

The Django middleware that does this is enabled by default. All you need to do
is include the {% csrf_token %} tag in your form template.

.. class:: incremental

Create a new file ``detail.html`` in your ``templates/polls`` directory

Detail Template
---------------

.. code-block:: django
    :class: small
    
    {% extends "base.html" %}
    {% block content %}
    <h1>{{ poll }}</h1>
    {% if poll.choice_set.count > 0 %}
    <form action="{% url poll_vote poll.pk %}" method="POST">
      {% csrf_token %}
      {% for choice in poll.choice_set.all %}
      <div class="choice">
        <label for="choice_{{ choice.pk }}">
          <input type="radio" name="choice" id="choice_{{ choice.pk }}" 
                 value="{{ choice.pk }}"/>
          {{ choice }}</label></div>
      {% endfor %}
      <input type="submit" name="vote" value="Vote"/>
    </form>
    {% else %}
    <p>No choices are available for this poll</p>
    {% endif %}
    {% endblock %}

Processing The Vote
-------------------

We can now submit a form to the ``poll_vote`` url. We need to process that
vote

.. class:: incremental

Here, a class-based generic view is just going to get in our way.  Let's use
an old-fashioned view function.

.. class:: incremental

How is our user's vote reaching the server?

.. class:: incremental

It gets there as POST data, the value for the key 'choice'.

Django GET and POST Data
------------------------

Django provides the same type of Request/Response based interaction model that
most frameworks are based on. Views are called with the first argument being a
``request`` object.

.. class:: incremental

request.GET and request.POST are dictionary-like objects containing data
parsed from incoming HTTP request.

.. class:: incremental

You can use normal dictionary syntax to read values from these:

.. code-block:: python
    :class: incremental small

    bar = request.POST['bucko']
    foo = request.GET.get('somevar', None)

Vote View Skeleton
------------------

In ``views.py`` from our ``polls`` app package:

.. code-block:: python
    :class: small

    from django.core.urlresolvers import reverse
    from django.http import HttpResponseRedirect

    def vote_view(request, pk):
        if request.method == "POST":
            try:
                # attempt to get a choice
            except NoGoodChoice: # send back to detail
                url = reverse('poll_detail', args=[pk, ])
            else: # vote and send to result
                url = reverse('poll_result', args=[pk])
        else: # submitted via GET, ignore it
            url = reverse('poll_detail', args=[pk, ])

        return HttpResponseRedirect(url)

Get the Choice
--------------

Let's start by filling out the process of getting the choice:

.. code-block:: python
    :class: small

    # add imports
    from django.shortcuts import get_object_or_404
    from django.contrib import messages
    from polls.models import Poll, Choice
    # and edit our skeleton
    def vote_view(request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        if request.method == "POST":
            try:
                choice = poll.choice_set.get(
                    pk=request.POST.get('choice', 0))
            except Choice.DoesNotExist:
                msg = "Ooops, pick a choice that exists, please"
                messages.add_message(request, messages.ERROR, msg)
                url = reverse('poll_detail', args=[pk, ])

Add a Vote
----------

Next, let's record a vote on our choice:

.. code-block:: python
    :class: small

    def vote_view(request, pk):
        ...
        try:
            # choice = ...
        except Choice.DoesNotExist:
            # ...
        else:
            choice.votes += 1
            choice.save()
            messages.add_message(request, messages.INFO,
                                 "You voted for %s" % choice)
            url = reverse('poll_result', args=[pk])

Add the URL
-----------

Finally, we need to add this view to our urlconf. Back in ``urls.py`` in the
``polls`` app package, edit the url for the voting view like so:

.. code-block:: python
    :class: small

    url(r'^(?P<pk>\d+)/vote/$',
        'polls.views.vote_view',
        name="poll_vote"),

.. class:: incremental

Notice that the 'callable' in this pattern is a string. Django allows you to
use this sort of *dotted name* reference. It will resolve it (or throw an
error if it can't)

Display Result
--------------

The last view we need is the poll result. This can simply be a different
version of the Generic DetailView. Still in ``urls.py`` edit the pattern for
the results view:

.. code-block:: python
    :class: small

    url(r'^(?P<pk>\d+)/result/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/result.html"),
        name="poll_result")

.. class:: incremental

And, of course, we will need to create that final template

Result Template
---------------

In ``templates/polls`` create a new file, ``result.html``:

.. code-block:: django
    :class: small

    {% extends "base.html" %}

    {% block content %}
    <h1>{{ poll }}</h1>
    <ul>
      {% for choice in poll.choice_set.all %}
      <li>{{ choice }} ({{choice.votes}} votes)</li>
      {% endfor %}
    </ul>
    <a href="{% url poll_list %}">Back to the polls, please</a>
    {% endblock %}

Play a Bit
----------

Alright. You've done it. 

Take a few minutes to add some polls in the Admin.

Then return to the public side and vote. See how it goes.

Next Week
---------

We are going to mix it up quite a bit this week.

.. class:: incremental

I would like you all to divide into teams. Each team should have 4-6 people.
Each team should have both experienced and inexperienced members. Try to match
up with people whose strengths are different from your own.

.. class:: incremental

Now, each team, pick a 'facilitator'. This person will be responsible for
managing the operation of the team. This person will help to ensure that each
team member has a task. This should be a more experienced team member.

Assignment
----------

During this week, each **non-leader member** will duplicate the Flaskr app
using Django.

.. class:: incremental

* Create a new *app* which will hold all the code required.
* Define the model for the 'entry' object.
* Extend that model with two additional fields: ``publication_date``
  (DateTimeField), and ``author`` (ForeignKey to
  ``django.contrib.auth.models.User``)
* Define the URLs you'll need (an entry list, a form processor)
* Define the Views you'll need (see the two above).

Assignment
----------

During this week, each **team leader** will communicate with me to build a
plan for implementing a new feature for the Django flaskr app.

.. class:: incremental

* User Registration
* 'Archive' views based on date or author
* WYSIWYG visual editor for entry posts.
* Tagging
* Theme (make it beautiful)
* Search (this is a bigger one than you might think)

Submitting the Assignment
-------------------------

Leaders, you will communicate with me to make a plan

Members, you will do the usual submission of your code.

DO NOT ATTEMPT TO GET YOUR CODE RUNNING ON A VM

Next Week
---------

Our class next week will be a little different. Each team will be implementing
a new feature for our micro-blog application.

We will work in teams for the entire class up until 8:30, when we will show
off our results.

