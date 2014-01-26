Jinja2 Template Introduction
============================

When you installed ``flask`` into your virtualenv, along with it came a
Python-based templating engine called ``Jinja2``.

In this walkthrough, you'll see some basics about how templates work, and get
to know what sorts of options they provide you for creating HTML from a Python
process.

Generating HTML
---------------

.. class:: big-centered

"I enjoy writing HTML in Python"

.. class:: incremental right

-- nobody, ever


Templating
----------

A good framework will provide some way of generating HTML with a templating
system.

.. class:: incremental

There are nearly as many templating systems as there are frameworks

.. class:: incremental

Each has advantages and disadvantages

.. class:: incremental

Flask includes the *Jinja2* templating system (perhaps because it's built by
the same folks)


Jinja2 Template Basics
----------------------

Let's start with the absolute basics.

.. container:: incremental

    Fire up a Python interpreter, using your flask virtualenv:
    
    .. code-block:: python
        :class: small
    
        (flaskenv)$ python
        >>> from jinja2 import Template

.. container:: incremental

    A template is built of a simple string:
    
    .. code-block:: python
        :class: small

        >>> t1 = Template("Hello {{ name }}, how are you?")


Rendering a Template
--------------------

Call the ``render`` method, providing some *context*:

.. code-block:: python
    :class: incremental small

    >>> t1.render(name="Freddy")
    u'Hello Freddy, how are you?'
    >>> t1.render({'name': "Roberto"})
    u'Hello Roberto, how are you?'
    >>>

.. class:: incremental

*Context* can either be keyword arguments, or a dictionary


Dictionaries in Context
-----------------------

Dictionaries passed in as part of the *context* can be addressed with *either*
subscript or dotted notation:

.. code-block:: python
    :class: incremental small

    >>> person = {'first_name': 'Frank',
    ...           'last_name': 'Herbert'}
    >>> t2 = Template("{{ person.last_name }}, {{ person['first_name'] }}")
    >>> t2.render(person=person)
    u'Herbert, Frank'

.. class:: incremental

* Jinja2 will try the *correct* way first (attr for dotted, item for
  subscript).
* If nothing is found, it will try the opposite.
* If nothing is found, it will return an *undefined* object.


Objects in Context
------------------

The exact same is true of objects passed in as part of *context*:

.. code-block:: python
    :class: incremental small

    >>> t3 = Template("{{ obj.x }} + {{ obj['y'] }} = Fun!")
    >>> class Game(object):
    ...   x = 'babies'
    ...   y = 'bubbles'
    ...
    >>> bathtime = Game()
    >>> t3.render(obj=bathtime)
    u'babies + bubbles = Fun!'

.. class:: incremental

This means your templates can be a bit agnostic as to the nature of the things
in *context*


Filtering values in Templates
-----------------------------

You can apply *filters* to the data passed in *context* with the pipe ('|')
operator:

.. code-block:: python
    :class: incremental small

    t4 = Template("shouted: {{ phrase|upper }}")
    >>> t4.render(phrase="this is very important")
    u'shouted: THIS IS VERY IMPORTANT'

.. container:: incremental

    You can also chain filters together:
    
    .. code-block:: python
        :class: small
    
        t5 = Template("confusing: {{ phrase|upper|reverse }}")
        >>> t5.render(phrase="howdy doody")
        u'confusing: YDOOD YDWOH'


Control Flow
------------

Logical control structures are also available:

.. code-block:: python
    :class: incremental small

    tmpl = """
    ... {% for item in list %}{{ item }}, {% endfor %}
    ... """
    >>> t6 = Template(tmpl)
    >>> t6.render(list=[1,2,3,4,5,6])
    u'\n1, 2, 3, 4, 5, 6, '

.. class:: incremental

Any control structure introduced in a template **must** be paired with an 
explicit closing tag ({% for %}...{% endfor %})


Template Tests
--------------

There are a number of specialized *tests* available for use with the
``if...elif...else`` control structure:

.. code-block:: python
    :class: incremental small

    >>> tmpl = """
    ... {% if phrase is upper %}
    ...   {{ phrase|lower }}
    ... {% elif phrase is lower %}
    ...   {{ phrase|upper }}
    ... {% else %}{{ phrase }}{% endif %}"""
    >>> t7 = Template(tmpl)
    >>> t7.render(phrase="FOO")
    u'\n\n  foo\n'
    >>> t7.render(phrase="bar")
    u'\n\n  BAR\n'
    >>> t7.render(phrase="This should print as-is")
    u'\nThis should print as-is'


Basic Python Expressions
------------------------

Basic Python expressions are also supported:

.. code-block:: python
    :class: incremental small

    tmpl = """
    ... {% set sum = 0 %}
    ... {% for val in values %}
    ... {{ val }}: {{ sum + val }}
    ...   {% set sum = sum + val %}
    ... {% endfor %}
    ... """
    >>> t8 = Template(tmpl)
    >>> t8.render(values=range(1,11))
    u'\n\n\n1: 1\n  \n\n2: 3\n  \n\n3: 6\n  \n\n4: 10\n
      \n\n5: 15\n  \n\n6: 21\n  \n\n7: 28\n  \n\n8: 36\n
      \n\n9: 45\n  \n\n10: 55\n  \n'


Much, Much More
---------------

There's more that Jinja2 templates can do, and you'll see more in class
when we write templates for our Flask app.

.. container:: incremental

    Make sure that you bookmark the Jinja2 documentation for later use::

        http://jinja.pocoo.org/docs/templates/
