SQL Persistence in Python
=========================

In this tutorial, you'll walk through some basic concepts of data persistence
using the Python stdlib implementation of DB API 2, `sqlite3`

Data Persistence
----------------

There are many models for persistance of data.

.. class:: incremental

* Flat files
* Relational Database (SQL RDBMs like PostgreSQL, MySQL, SQLServer, Oracle)
* Object Stores (Pickle, ZODB)
* NoSQL Databases (CouchDB, MongoDB, etc)

.. class:: incremental

It's also one of the most contentious issues in app design.

.. class:: incremental

For this reason, it's one of the things that most Small Frameworks leave
undecided.


Simple SQL
----------

`PEP 249 <http://www.python.org/dev/peps/pep-0249/>`_ describes a
common API for database connections called DB-API 2.

.. container:: incremental

    The goal was to

        achieve a consistency leading to more easily understood modules, code
        that is generally more portable across databases, and a broader reach
        of database connectivity from Python

        .. class:: image-credit

        source: http://www.python.org/dev/peps/pep-0248/


A Note on DB API
----------------

.. class:: incremental center

It is important to remember that PEP 249 is **only a specification**.

.. class:: incremental

There is no code or package for DB-API 2 on it's own.

.. class:: incremental

Since 2.5, the Python Standard Library has provided a `reference
implementation of the api <http://docs.python.org/2/library/sqlite3.html>`_
based on SQLite3

.. class:: incremental

Before Python 2.5, this package was available as ``pysqlite``


Using DB API
------------

To use the DB API with any database other than SQLite3, you must have an
underlying API package available.

.. container:: incremental

    Implementations are available for:

    * PostgreSQL (**psycopg2**, txpostgres, ...)
    * MySQL (**mysql-python**, PyMySQL, ...)
    * MS SQL Server (**adodbapi**, pymssql, mxODBC, pyodbc, ...)
    * Oracle (**cx_Oracle**, mxODBC, pyodbc, ...)
    * and many more...

    .. class:: image-credit

    source: http://wiki.python.org/moin/DatabaseInterfaces


Installing API Packages
-----------------------

Most db api packages can be installed using typical Pythonic methods::

    $ easy_install psycopg2
    $ pip install mysql-python
    ...

.. class:: incremental

Most api packages will require that the development headers for the underlying
database system be available. Without these, the C symbols required for
communication with the db are not present and the wrapper cannot work.


Not Today
---------

We don't want to spend the next hour getting a package installed, so let's use
``sqlite3`` instead.

.. class:: incremental

I **do not** recommend using sqlite3 for production web applications, there are
too many ways in which it falls short

.. class:: incremental

But it will provide a solid learning tool


Getting Started
---------------

In the class resources folder, you'll find an ``sql`` directory. Copy that to
your working directory.

.. class:: incremental

Open the file ``createdb.py`` in your text editor.  Edit ``main`` like so:

.. code-block:: python
    :class: incremental small

    def main():
        conn =  sqlite3.connect(DB_FILENAME)
        if DB_IS_NEW:
            print 'Need to create database and schema'
        else:
            print 'Database exists, assume schema does, too.'
        conn.close()


Try It Out
----------

Run the ``createdb.py`` script to see it in effect::

    $ python createdb.py
    Need to create database and schema
    $ python createdb.py
    Database exists, assume schema does, too.
    $ ls
    books.db
    ...

.. class:: incremental

Sqlite3 will automatically create a new database when you connect for the
first time, if one does not exist.


Set Up A Schema
---------------

Make the following changes to ``createdb.py``:

.. code-block:: python
    :class: small

    DB_FILENAME = 'books.db'
    SCHEMA_FILENAME = 'ddl.sql' # <- this is new
    DB_IS_NEW = not os.path.exists(DB_FILENAME)

    def main():
        with sqlite3.connect(DB_FILENAME) as conn: # <- context mgr
            if DB_IS_NEW: # A whole new if clause:
                print 'Creating schema'
                with open(SCHEMA_FILENAME, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)
            else:
                print 'Database exists, assume schema does, too.'
        # delete the `conn.close()` that was here.


Verify Your Work
----------------

Quit your python interpreter and delete the file ``books.db``

.. container:: incremental

    Then run the script from the command line again to try it out::

        $ python createdb.py
        Creating schema
        $ python createdb.py
        Database exists, assume schema does, too.

Introspect the Database
-----------------------

Add the following to ``createdb.py``:

.. code-block:: python
    :class: small

    # in the imports, add this line:
    from utils import show_table_metadata

    else:
        # in the else clause, replace the print statement with this:
        print "Database exists, introspecting:"
        tablenames = ['author', 'book']
        cursor = conn.cursor()
        for name in tablenames:
            print "\n"
            show_table_metadata(cursor, name)

.. class:: incremental

Then try running ``python createdb.py`` again

My Results
----------

.. class:: small

::

    $ python createdb.py
    Table Metadata for 'author':
    cid        | name       | type       | notnull    | dflt_value | pk         |
    -----------+------------+------------+------------+------------+------------+-
    0          | authorid   | INTEGER    | 1          | None       | 1          |
    -----------+------------+------------+------------+------------+------------+-
    1          | name       | TEXT       | 0          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-


    Table Metadata for 'book':
    cid        | name       | type       | notnull    | dflt_value | pk         |
    -----------+------------+------------+------------+------------+------------+-
    0          | bookid     | INTEGER    | 1          | None       | 1          |
    -----------+------------+------------+------------+------------+------------+-
    1          | title      | TEXT       | 0          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-
    2          | author     | INTEGER    | 1          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-


Inserting Data
--------------

Let's load up some data. Fire up your interpreter and type:

.. code-block:: python
    :class: small

    >>> import sqlite3
    >>> insert = """
    ... INSERT INTO author (name) VALUES("Iain M. Banks");"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(insert)
    ...     cur.rowcount
    ...     cur.close()
    ...     
    <sqlite3.Cursor object at 0x10046e880>
    1
    >>> 

.. class:: incremental

Did that work?


Querying Data
-------------

Let's query our database to find out:

.. code-block:: python
    :class: small

    >>> query = """
    ... SELECT * from author;"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(query)
    ...     rows = cur.fetchall()
    ...     for row in rows:
    ...         print row
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    (1, u'Iain M. Banks')

.. class:: incremental

Alright!  We've got data in there.  Let's make it more efficient


Parameterized Statements
------------------------

Try this:

.. code-block:: python
    :class: small

    >>> insert = """
    ... INSERT INTO author (name) VALUES(?);"""
    >>> authors = [["China Mieville"], ["Frank Herbert"],
    ... ["J.R.R. Tolkien"], ["Susan Cooper"], ["Madeline L'Engle"]]
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.executemany(insert, authors)
    ...     print cur.rowcount
    ...     cur.close()
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    5


Check Your Work
---------------

Again, query the database:

.. code-block:: python
    :class: small

    >>> query = """
    ... SELECT * from author;"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(query)
    ...     rows = cur.fetchall()
    ...     for row in rows:
    ...         print row
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    (1, u'Iain M. Banks')
    ...
    (4, u'J.R.R. Tolkien')
    (5, u'Susan Cooper')
    (6, u"Madeline L'Engle")


Transactions
------------

Transactions group operations together, allowing you to verify them *before*
the results hit the database.

.. class:: incremental

In SQLite3, data-altering statements require an explicit ``commit`` unless
auto-commit has been enabled.

.. class:: incremental

The ``with`` statements we've used take care of committing when the context
manager closes.

.. class:: incremental

Let's change that so we can see what happens explicitly


Populating the Database
-----------------------

Let's start by seeing what happens when you try to look for newly added data
before the ``insert`` transaction is committed.

.. class:: incremental

Begin by quitting your interpreter and deleting ``books.db``.  

.. container:: incremental

    Then re-create the database, empty::

        $ python createdb.py
        Creating schema


Setting Up the Test
-------------------

.. class:: small

Open ``populatedb.py`` in your editor, replace the final ``print``:

.. code-block:: python
    :class: small

    conn1 = sqlite3.connect(DB_FILENAME)
    conn2 = sqlite3.connect(DB_FILENAME)
    print "\nOn conn1, before insert:"
    show_authors(conn1)
    authors = ([author] for author in AUTHORS_BOOKS.keys())
    cur = conn1.cursor()
    cur.executemany(author_insert, authors)
    print "\nOn conn1, after insert:"
    show_authors(conn1)
    print "\nOn conn2, before commit:"
    show_authors(conn2)
    conn1.commit()
    print "\nOn conn2, after commit:"
    show_authors(conn2)
    conn1.close()
    conn2.close()


Running the Test
----------------

.. class:: small

Quit your python interpreter and run the ``populatedb.py`` script:

.. class:: small incremental

::

    On conn1, before insert:
    no rows returned
    On conn1, after insert:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")

    On conn2, before commit:
    no rows returned
    On conn2, after commit:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")


Rollback
--------

That's all well and good, but what happens if an error occurs?

.. class:: incremental

Transactions can be rolled back in order to wipe out partially completed work.

.. class:: incremental

Like with commit, using ``connect`` as a context manager in a ``with``
statement will automatically rollback for exceptions.

.. class:: incremental

Let's rewrite our populatedb script so it explicitly commits or rolls back a
transaction depending on exceptions occurring


Edit populatedb.py (slide 1)
----------------------------

.. class:: small

First, add the following function above the ``if __name__ == '__main__'``
block:

.. code-block:: python
    :class: small

    def populate_db(conn):
        authors = ([author] for author in AUTHORS_BOOKS.keys())
        cur = conn.cursor()
        cur.executemany(author_insert, authors)

        for author in AUTHORS_BOOKS.keys():
            params = ([book, author] for book in AUTHORS_BOOKS[author])
            cur.executemany(book_insert, params)


Edit populatedb.py (slide 2)
----------------------------

.. class:: small

Then, in the runner:

.. code-block:: python
    :class: small

    with sqlite3.connect(DB_FILENAME) as conn1:
        with sqlite3.connect(DB_FILENAME) as conn2:
            try:
                populate_db(conn1)
                print "\nauthors and books on conn2 before commit:"
                show_authors(conn2)
                show_books(conn2)
            except sqlite3.Error:
                conn1.rollback()
                print "\nauthors and books on conn2 after rollback:"
                show_authors(conn2)
                show_books(conn2)
                raise
            else:
                conn1.commit()
                print "\nauthors and books on conn2 after commit:"
                show_authors(conn2)
                show_books(conn2)


Try it Out
----------

Remove ``books.db`` and recrete the database, then run our script:

.. class:: small

::

    $ rm books.db
    $ python createdb.py
    Creating schema
    $ python populatedb.py

.. class:: small incremental

::

    authors and books on conn2 after rollback:
    no rows returned
    no rows returned
    Traceback (most recent call last):
      File "populatedb.py", line 57, in <module>
        populate_db(conn1)
      File "populatedb.py", line 46, in populate_db
        cur.executemany(book_insert, params)
    sqlite3.InterfaceError: Error binding parameter 0 - probably unsupported type.

Oooops, Fix It
--------------

.. class:: small

Okay, we got an error, and the transaction was rolled back correctly.

.. container:: incremental small

    Open ``utils.py`` and find this:

    .. code-block:: python 

        'Susan Cooper': ["The Dark is Rising", ["The Greenwitch"]],

.. container:: incremental small

    Fix it like so:

    .. code-block:: python

        'Susan Cooper': ["The Dark is Rising", "The Greenwitch"],

.. class:: small incremental

It appears that we were attempting to bind a list as a parameter.  Ooops.


Try It Again
------------

.. container:: small

    Now that the error in our data is repaired, let's try again::

        $ python populatedb.py

.. class:: small incremental

::

    Reporting authors and books on conn2 before commit:
    no rows returned
    no rows returned
    Reporting authors and books on conn2 after commit:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")
    (1, u'Perdido Street Station', 1)
    (2, u'The Scar', 1)
    (3, u'King Rat', 1)
    (4, u'Dune', 2)
    (5, u"Hellstrom's Hive", 2)
    (6, u'The Dark is Rising', 3)
    (7, u'The Greenwitch', 3)
    (8, u'The Hobbit', 4)
    (9, u'The Silmarillion', 4)
    (10, u'A Wrinkle in Time', 5)
    (11, u'A Swiftly Tilting Planet', 5)

Congratulations
---------------

You've just created a small database of books and authors. The transactional
protections you've used let you rest comfortable, knowing that so long as the
process completed, you've got the data you sent.

We'll see more of this when we build our flask app.
