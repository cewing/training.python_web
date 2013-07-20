Internet Programming with Python
================================

blah blah blah

Templates in Flask
------------------

Use the ``render_template`` function:

.. code-block:: python
    :class: small

    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

.. class:: incremental

Flask looks for a ``templates`` directory in the same location as your app
module (remember ``app = Flask(__name__)``?).

.. class:: incremental

Any extra variables you want to pass to the template should be keyword
arguments to ``render_template``

Flask Template Context
----------------------

Flask adds a few things to the context of templates.  You can use these

.. class:: incremental

* **config**: contains the current configuration object
* **request**: contains the current request object
* **session**: any session data that might be available
* **g**: the request-local object to which global variables are bound
* **get_flashed_messages**: a function that returns messages you flash to your
  users (more on this later).
* **url_for**: so you can easily *reverse* urls from within your templates

Lab 1
-----

Open a terminal, change directories to the class repository, then to
``assignments/week05/lab/book_app``.

.. class:: incremental

* You'll find a file ``book_app.py`` which is all set up and ready to go
* You'll also find a ``templates`` directory with some templates
* Complete the functions to provide the right stuff to the templates
* Complete the templates to display the data to the end-user
* At the end you should have a reproduced version of last week's homework

.. class:: incremental center

**GO**





Lab 2 - Part 3
--------------

Now we can read and write blog entries, let's add views so we can see what
we're doing.

.. class:: incremental

Again.  Tests come first.

.. class:: incremental

And again, if you've fallen behind or want to start clean, the completed code
from our last step is in ``flaskr_3``

Test the Front Page
-------------------

Add the following tests to ``flaskr_tests.py``:

.. code-block::

    def test_empty_listing(self):
        rv = self.client.get('/')
        assert 'No entries here so far' in rv.data

    def test_listing(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.write_entry(*expected)
        rv = self.client.get('/')
        for value in expected:
            assert value in rv.data

Template Inheritance
--------------------

One aspect of Jinja2 templates we haven't seen yet is that templates can
inherit structure from other templates.

.. class:: incremental

* you can make replaceable blocks in templates with blocks: ``{% block foo
  %}{% endblock %}``.
* you can build on a template in a second template by extending: ``{% extends
  "layout.html" %}`` (this *must* be first)

.. class:: incremental

We want the parts of our app to look alike, so let's create a basic layout
first.  Create a file ``layout.html`` in the ``templates`` directory.

Creating Layout
---------------

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
      <head>
        <title>Flaskr</title>
      </head>
      <body>
        <h1>Flaskr</h1>
        <div class="content">
        {% block body %}{% endblock %}
        </div>
      </body>
    </html>

Extending Layout
----------------

Create a new file, ``show_entries.html`` in ``templates``:

.. code-block:: jinja
    :class: small

    {% extends "layout.html" %}
    {% block body %}
      <h2>Posts</h2>
      <ul class="entries">
      {% for entry in entries %}
        <li>
          <h2>{{ entry.title }}</h2>
          <div class="entry_body">
          {{ entry.text|safe }}
          </div>
        </li>
      {% else %}
        <li><em>No entries here so far</em></li>
      {% endfor %}
      </ul>
    {% endblock %}

Creating a View
---------------

Now, we just need to hook up our entries to that template. In ``flaskr.py``
add the following code:

.. code-block:: python

    # at the top, import
    from flask import render_template

    # and after our last functions:
    @app.route('/')
    def show_entries():
        entries = get_all_entries()
        return render_template('show_entries.html', entries=entries)

.. class:: incremental

Run our tests.  Should be 6 for 6 now.

Authentication
--------------

We don't want just anyone to be able to add new entries. So we want to be able
to authenticate a user.

.. class:: incremental

We'll be using built-in functionality of Flask to do this, but this
simplest-possible implementation should serve only as a guide.

.. class:: incremental

We'll start with the tests, of course.

Test Authentication
-------------------

Back in ``flaskr_tests.py`` add new test methods:

.. code-block:: python
    :class: small

    def test_login_passes(self):
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.do_login(flaskr.app.config['USERNAME'],
                            flaskr.app.config['PASSWORD'])
            self.assertTrue(session.get('logged_in', False))

    def test_login_fails(self):
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            self.assertRaises(ValueError, flaskr.do_login,
                              flaskr.app.config['USERNAME'],
                              'incorrectpassword')

Set Up Authentication
---------------------

Now, let's add the code in ``flaskr.py`` to support this:

.. code-block:: python
    :class: small

    # add an import
    from flask import session

    # and configuration
    USERNAME = 'admin'
    PASSWORD = 'default'

    # and a function
    def do_login(usr, pwd):
        if usr != app.config['USERNAME']:
            raise ValueError
        elif pwd != app.config['PASSWORD']:
            raise ValueError
        else:
            session['logged_in'] = True

Login/Logout in Tests
---------------------

Let's add tests for a view. We'll set up a form that redirects back to the
main view on success. First, methods to actually do the login/logout (in
``flaskr_tests.py``):

.. code-block:: python

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout',
                               follow_redirects=True)

Test Authentication
-------------------

And now the test itself (again, ``flaskr_tests.py``):

.. code-block:: python

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid Login' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid Login' in rv.data

.. class:: incremental

We should be up to 9 tests, one failing

Add Login Template
------------------

Add ``login.html`` to ``templates``:

.. code-block:: jinja
    :class: tiny

    {% extends "layout.html" %}
    {% block body %}
      <h2>Login</h2>
      {% if error -%}
        <p class="error"><strong>Error</strong> {{ error }}
      {%- endif %}
      <form action="{{ url_for('login') }}" method="POST">
        <div class="field">
          <label for="username">Username</label>
          <input type="text" name="username" id="username"/>
        </div>
        <div class="field">
          <label for="password">Password</label>
          <input type="password" name="password" id="password"/>
        </div>
        <div class="control_row">
          <input type="submit" name="Login" value="Login"/>
        </div>
      </form>
    {% endblock %}

Add Login/Logout Views
----------------------

And back in ``flaskr.py`` add new code.  Let's start with imports:

.. code-block:: python

    # at the top, new imports
    from flask import request
    from flask import redirect
    from flask import flash
    from flask import url_for

And the View Code
-----------------

.. code-block:: python
    :class: small

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            try:
                do_login(request.form['username'],
                         request.form['password'])
            except ValueError:
                error = "Invalid Login"
            else:
                flash('You were logged in')
                return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))

About Flash
-----------

.. class:: small

Flask provides ``flash`` as a way of sending messages to the user from view
code. We need a place to show these messages. Add it to ``layout.html`` (along
with links to log in and out)

.. code-block:: jinja
    :class: small

    <h1>Flaskr</h1>       <!-- already there -->
    <div class="metanav"> <!-- add all this -->
    {% if not session.logged_in %}
      <a href="{{ url_for('login') }}">log in</a>
    {% else %}
      <a href="{{ url_for('logout') }}">log_out</a>
    {% endif %}
    </div>
    {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
    {% endfor %}
    <div class="content"> <!-- already there -->

Adding an Entry
---------------

We still lack a way to add an entry. We need a view to do that. Again, tests
first (in ``flaskr_tests.py``):

.. code-block:: python

    def test_add_entries(self):
        self.login('admin', 'default')
        rv = self.client.post('/add', data=dict(
            title='Hello',
            text='This is a post'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert 'Hello' in rv.data
        assert 'This is a post' in rv.data

Add the View
------------

We've already got all the stuff we need to write entries, we just need an
endpoint that will do it via the web (in ``flaskr.py``):

.. code-block:: python
    :class: small

    # add an import
    from flask import abort

    @app.route('/add', methods=['POST'])
    def add_entry():
        if not session.get('logged_in'):
            abort(401)
        try:
            write_entry(request.form['title'], request.form['text'])
            flash('New entry was successfully posted')
        except sqlite3.Error as e:
            flash('There was an error: %s' % e.args[0])
        return redirect(url_for('show_entries'))

Where do Entries Come From
--------------------------

Finally, we're almost done. We can log in and log out. We can add entries and
view them. But look at that last view. Do you see a call to
``render_template`` in there at all?

.. class:: incremental

There isn't one. That's because that view is never meant to be be visible.
Look carefully at the logic. What happens?

.. class:: incremental

So where do the form values come from?

.. class:: incremental

Let's add a form to the main view.  Open ``show_entries.html``

Provide a Form
--------------

.. code-block:: jinja
    :class: small

    {% block body %}  <!-- already there -->
    {% if session.logged_in %}
    <form action="{{ url_for('add_entry') }}" method="POST" class="add_entry">
      <div class="field">
        <label for="title">Title</label>
        <input type="text" size="30" name="title" id="title"/>
      </div>
      <div class="field">
        <label for="text">Text</label>
        <textarea name="text" id="text" rows="5" cols="80"></textarea>
      </div>
      <div class="control_row">
        <input type="submit" value="Share" name="Share"/>
      </div>
    </form>
    {% endif %}
    <h2>Posts</h2>  <!-- already there -->

All Done
--------

Okay.  That's it.  We've got an app all written.

.. class:: incremental

So far, we haven't actually touched our browsers at all, but we have
reasonable certainty that this works because of our tests. Let's try it.


.. class:: incremental

In the terminal where you've been running tests, run our flaskr app:

.. class:: incremental

::

    (flaskenv)$ python flaskr.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

The Big Payoff
--------------

Now load ``http://localhost:5000/`` in your browser and enjoy your reward.

Lab 2 - Part 4
--------------

On the other hand, what we've got here is pretty ugly.  We could prettify it.

.. class:: incremental

Again, if you want to start fresh or you fell behind you can find code
completed to this point in ``flaskr_4``.

.. class:: incremental

In that directory inside the ``static`` directory you will find
``styles.css``. Open it in your editor.  It contains basic CSS for this app.

.. class:: incremental

We'll need to include this file in our ``layout.html``.

Static Files
------------

Like page templates, Flask locates static resources like images, css and
javascript by looking for a ``static`` directory next to the app module.

.. class:: incremental

You can use the special url endpoint ``static`` to build urls that point here.
Open ``layout.html`` and add the following:

.. code-block:: jinja
    :class: small incremental

    <head>  <!-- you only need to add the <link> below -->
      <title>Flaskr</title>
      <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" type="text/css">
    </head>


Deploying
---------

First, move the source code to your VM::

    (flaskenv)$ cd ../
    (flaskenv)$ tar -czvf flaskr.tgz flaskr
    (flaskenv)$ scp flaskr.tgz <your_vm>:~/
    (flaskenv)$ ssh <your_vm>
    $ tar -zxvf flaskr.tgz

Then, on your VM, set up a virtualenv with Flask installed

Deploying
---------

You'll need to make some changes to mod_wsgi configuration.

* Open ``/etc/apache2/sites-available/default`` in an editor (on the VM)

* Add the following line at the top (outside the VirtualHost block):
  ``WSGIPythonHome /path/to/flaskenv``

* Delete all other lines refering to mod_wsgi configuration
* Add the following in the VirtualHost block:

::

    WSGIScriptAlias / /var/www/flaskr.wsgi

Deploying
---------

Finally, you'll need to add the named wsgi file and edit it to match::

    $ sudo touch /var/www/flaskr.wsgi
    $ sudo vi /var/www/flasrk.wsgi


    import sys
    sys.path.insert(0, 'path/to/flaskr') # the flaskr app you uploaded

    from flaskr import app as application

Deploying
---------

Finally, restart apache and bask in the glow::

    $ sudo apache2ctl configtest
    $ sudo /etc/init.d/apache2 graceful

Load http://your_vm/

Wheeee!

Going Further
-------------

It's not too hard to see ways you could improve this.

.. class:: incremental

* For my part, I made a version using Bootstrap.js.
* You could limit the number of posts shown on the front page.
* You could add dates to the posts and provide archived views for older posts.
* You could add the ability to edit existing posts (and add an updated date to the schema)
* ...

But Instead
-----------

Instead of doing any of that, this week's assignment is a bit different.

.. class:: incremental

You've implemented an app in one Small Framework. I want you to do it all
again, in a different Small Framework.

.. class:: incremental

While you're working on it, think about the differences between your new
Framework and Flask. What do you like more? What do you like less? How might
this influence your choice of Frameworks in the future?

Assignment
----------

* Re-implement the Flaskr app we built in class in a different Small
  Framework.
* There are several named in the class outline, and in this presentation.
* Pick one of them, or a different one of your choice.  It must be Python.
* When you are finished, add your source code and a README that talks about
  your experience to the ``athome`` folder of week05.
* Tell me about your new Framework. Discuss the points above regarding
  differences.

Submitting The Assignment
-------------------------

* Try to get your code running on your VM
* Add your source code, in it's entirety, to the ``athome`` folder for week 5
* Add a README.txt file that discusses the experience.
* Commit your changes to your fork of the class repository and send me a pull
  request
