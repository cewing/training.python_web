<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="generator" content="Docutils 0.11: http://docutils.sourceforge.net/" />
<title>SQL Persistence in Python</title>
<style type="text/css">

/*
:Author: David Goodger (goodger@python.org)
:Id: $Id: html4css1.css 7614 2013-02-21 15:55:51Z milde $
:Copyright: This stylesheet has been placed in the public domain.

Default cascading style sheet for the HTML output of Docutils.

See http://docutils.sf.net/docs/howto/html-stylesheets.html for how to
customize this style sheet.
*/

/* used to remove borders from tables and images */
.borderless, table.borderless td, table.borderless th {
  border: 0 }

table.borderless td, table.borderless th {
  /* Override padding for "table.docutils td" with "! important".
     The right padding separates the table cells. */
  padding: 0 0.5em 0 0 ! important }

.first {
  /* Override more specific margin styles with "! important". */
  margin-top: 0 ! important }

.last, .with-subtitle {
  margin-bottom: 0 ! important }

.hidden {
  display: none }

a.toc-backref {
  text-decoration: none ;
  color: black }

blockquote.epigraph {
  margin: 2em 5em ; }

dl.docutils dd {
  margin-bottom: 0.5em }

object[type="image/svg+xml"], object[type="application/x-shockwave-flash"] {
  overflow: hidden;
}

/* Uncomment (and remove this text!) to get bold-faced definition list terms
dl.docutils dt {
  font-weight: bold }
*/

div.abstract {
  margin: 2em 5em }

div.abstract p.topic-title {
  font-weight: bold ;
  text-align: center }

div.admonition, div.attention, div.caution, div.danger, div.error,
div.hint, div.important, div.note, div.tip, div.warning {
  margin: 2em ;
  border: medium outset ;
  padding: 1em }

div.admonition p.admonition-title, div.hint p.admonition-title,
div.important p.admonition-title, div.note p.admonition-title,
div.tip p.admonition-title {
  font-weight: bold ;
  font-family: sans-serif }

div.attention p.admonition-title, div.caution p.admonition-title,
div.danger p.admonition-title, div.error p.admonition-title,
div.warning p.admonition-title, .code .error {
  color: red ;
  font-weight: bold ;
  font-family: sans-serif }

/* Uncomment (and remove this text!) to get reduced vertical space in
   compound paragraphs.
div.compound .compound-first, div.compound .compound-middle {
  margin-bottom: 0.5em }

div.compound .compound-last, div.compound .compound-middle {
  margin-top: 0.5em }
*/

div.dedication {
  margin: 2em 5em ;
  text-align: center ;
  font-style: italic }

div.dedication p.topic-title {
  font-weight: bold ;
  font-style: normal }

div.figure {
  margin-left: 2em ;
  margin-right: 2em }

div.footer, div.header {
  clear: both;
  font-size: smaller }

div.line-block {
  display: block ;
  margin-top: 1em ;
  margin-bottom: 1em }

div.line-block div.line-block {
  margin-top: 0 ;
  margin-bottom: 0 ;
  margin-left: 1.5em }

div.sidebar {
  margin: 0 0 0.5em 1em ;
  border: medium outset ;
  padding: 1em ;
  background-color: #ffffee ;
  width: 40% ;
  float: right ;
  clear: right }

div.sidebar p.rubric {
  font-family: sans-serif ;
  font-size: medium }

div.system-messages {
  margin: 5em }

div.system-messages h1 {
  color: red }

div.system-message {
  border: medium outset ;
  padding: 1em }

div.system-message p.system-message-title {
  color: red ;
  font-weight: bold }

div.topic {
  margin: 2em }

h1.section-subtitle, h2.section-subtitle, h3.section-subtitle,
h4.section-subtitle, h5.section-subtitle, h6.section-subtitle {
  margin-top: 0.4em }

h1.title {
  text-align: center }

h2.subtitle {
  text-align: center }

hr.docutils {
  width: 75% }

img.align-left, .figure.align-left, object.align-left {
  clear: left ;
  float: left ;
  margin-right: 1em }

img.align-right, .figure.align-right, object.align-right {
  clear: right ;
  float: right ;
  margin-left: 1em }

img.align-center, .figure.align-center, object.align-center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.align-left {
  text-align: left }

.align-center {
  clear: both ;
  text-align: center }

.align-right {
  text-align: right }

/* reset inner alignment in figures */
div.align-right {
  text-align: inherit }

/* div.align-center * { */
/*   text-align: left } */

ol.simple, ul.simple {
  margin-bottom: 1em }

ol.arabic {
  list-style: decimal }

ol.loweralpha {
  list-style: lower-alpha }

ol.upperalpha {
  list-style: upper-alpha }

ol.lowerroman {
  list-style: lower-roman }

ol.upperroman {
  list-style: upper-roman }

p.attribution {
  text-align: right ;
  margin-left: 50% }

p.caption {
  font-style: italic }

p.credits {
  font-style: italic ;
  font-size: smaller }

p.label {
  white-space: nowrap }

p.rubric {
  font-weight: bold ;
  font-size: larger ;
  color: maroon ;
  text-align: center }

p.sidebar-title {
  font-family: sans-serif ;
  font-weight: bold ;
  font-size: larger }

p.sidebar-subtitle {
  font-family: sans-serif ;
  font-weight: bold }

p.topic-title {
  font-weight: bold }

pre.address {
  margin-bottom: 0 ;
  margin-top: 0 ;
  font: inherit }

pre.literal-block, pre.doctest-block, pre.math, pre.code {
  margin-left: 2em ;
  margin-right: 2em }

pre.code .ln { color: grey; } /* line numbers */
pre.code, code { background-color: #eeeeee }
pre.code .comment, code .comment { color: #5C6576 }
pre.code .keyword, code .keyword { color: #3B0D06; font-weight: bold }
pre.code .literal.string, code .literal.string { color: #0C5404 }
pre.code .name.builtin, code .name.builtin { color: #352B84 }
pre.code .deleted, code .deleted { background-color: #DEB0A1}
pre.code .inserted, code .inserted { background-color: #A3D289}

span.classifier {
  font-family: sans-serif ;
  font-style: oblique }

span.classifier-delimiter {
  font-family: sans-serif ;
  font-weight: bold }

span.interpreted {
  font-family: sans-serif }

span.option {
  white-space: nowrap }

span.pre {
  white-space: pre }

span.problematic {
  color: red }

span.section-subtitle {
  /* font-size relative to parent (h1..h6 element) */
  font-size: 80% }

table.citation {
  border-left: solid 1px gray;
  margin-left: 1px }

table.docinfo {
  margin: 2em 4em }

table.docutils {
  margin-top: 0.5em ;
  margin-bottom: 0.5em }

table.footnote {
  border-left: solid 1px black;
  margin-left: 1px }

table.docutils td, table.docutils th,
table.docinfo td, table.docinfo th {
  padding-left: 0.5em ;
  padding-right: 0.5em ;
  vertical-align: top }

table.docutils th.field-name, table.docinfo th.docinfo-name {
  font-weight: bold ;
  text-align: left ;
  white-space: nowrap ;
  padding-left: 0 }

/* "booktabs" style (no vertical lines) */
table.docutils.booktabs {
  border: 0px;
  border-top: 2px solid;
  border-bottom: 2px solid;
  border-collapse: collapse;
}
table.docutils.booktabs * {
  border: 0px;
}
table.docutils.booktabs th {
  border-bottom: thin solid;
  text-align: left;
}

h1 tt.docutils, h2 tt.docutils, h3 tt.docutils,
h4 tt.docutils, h5 tt.docutils, h6 tt.docutils {
  font-size: 100% }

ul.auto-toc {
  list-style-type: none }

</style>
</head>
<body>
<div class="document" id="sql-persistence-in-python">
<h1 class="title">SQL Persistence in Python</h1>

<p>In this tutorial, you'll walk through some basic concepts of data persistence
using the Python stdlib implementation of DB API 2, <cite>sqlite3</cite></p>
<div class="section" id="data-persistence">
<h1>Data Persistence</h1>
<p>There are many models for persistance of data.</p>
<ul class="incremental simple">
<li>Flat files</li>
<li>Relational Database (SQL RDBMs like PostgreSQL, MySQL, SQLServer, Oracle)</li>
<li>Object Stores (Pickle, ZODB)</li>
<li>NoSQL Databases (CouchDB, MongoDB, etc)</li>
</ul>
<p class="incremental">It's also one of the most contentious issues in app design.</p>
<p class="incremental">For this reason, it's one of the things that most Small Frameworks leave
undecided.</p>
</div>
<div class="section" id="simple-sql">
<h1>Simple SQL</h1>
<p><a class="reference external" href="http://www.python.org/dev/peps/pep-0249/">PEP 249</a> describes a
common API for database connections called DB-API 2.</p>
<div class="incremental container">
<p>The goal was to</p>
<blockquote>
<p>achieve a consistency leading to more easily understood modules, code
that is generally more portable across databases, and a broader reach
of database connectivity from Python</p>
<p class="image-credit">source: <a class="reference external" href="http://www.python.org/dev/peps/pep-0248/">http://www.python.org/dev/peps/pep-0248/</a></p>
</blockquote>
</div>
</div>
<div class="section" id="a-note-on-db-api">
<h1>A Note on DB API</h1>
<p class="incremental center">It is important to remember that PEP 249 is <strong>only a specification</strong>.</p>
<p class="incremental">There is no code or package for DB-API 2 on it's own.</p>
<p class="incremental">Since 2.5, the Python Standard Library has provided a <a class="reference external" href="http://docs.python.org/2/library/sqlite3.html">reference
implementation of the api</a>
based on SQLite3</p>
<p class="incremental">Before Python 2.5, this package was available as <tt class="docutils literal">pysqlite</tt></p>
</div>
<div class="section" id="using-db-api">
<h1>Using DB API</h1>
<p>To use the DB API with any database other than SQLite3, you must have an
underlying API package available.</p>
<div class="incremental container">
<p>Implementations are available for:</p>
<ul class="simple">
<li>PostgreSQL (<strong>psycopg2</strong>, txpostgres, ...)</li>
<li>MySQL (<strong>mysql-python</strong>, PyMySQL, ...)</li>
<li>MS SQL Server (<strong>adodbapi</strong>, pymssql, mxODBC, pyodbc, ...)</li>
<li>Oracle (<strong>cx_Oracle</strong>, mxODBC, pyodbc, ...)</li>
<li>and many more...</li>
</ul>
<p class="image-credit">source: <a class="reference external" href="http://wiki.python.org/moin/DatabaseInterfaces">http://wiki.python.org/moin/DatabaseInterfaces</a></p>
</div>
</div>
<div class="section" id="installing-api-packages">
<h1>Installing API Packages</h1>
<p>Most db api packages can be installed using typical Pythonic methods:</p>
<pre class="literal-block">
$ easy_install psycopg2
$ pip install mysql-python
...
</pre>
<p class="incremental">Most api packages will require that the development headers for the underlying
database system be available. Without these, the C symbols required for
communication with the db are not present and the wrapper cannot work.</p>
</div>
<div class="section" id="not-today">
<h1>Not Today</h1>
<p>We don't want to spend the next hour getting a package installed, so let's use
<tt class="docutils literal">sqlite3</tt> instead.</p>
<p class="incremental">I <strong>do not</strong> recommend using sqlite3 for production web applications, there are
too many ways in which it falls short</p>
<p class="incremental">But it will provide a solid learning tool</p>
</div>
<div class="section" id="getting-started">
<h1>Getting Started</h1>
<p>In the class resources folder, you'll find an <tt class="docutils literal">sql</tt> directory. Copy that to
your working directory.</p>
<p class="incremental">Open the file <tt class="docutils literal">createdb.py</tt> in your text editor.  Edit <tt class="docutils literal">main</tt> like so:</p>
<pre class="code python incremental small literal-block">
<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
    <span class="n">conn</span> <span class="o">=</span>  <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">DB_IS_NEW</span><span class="p">:</span>
        <span class="k">print</span> <span class="s">'Need to create database and schema'</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">print</span> <span class="s">'Database exists, assume schema does, too.'</span>
    <span class="n">conn</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre>
</div>
<div class="section" id="try-it-out">
<h1>Try It Out</h1>
<p>Run the <tt class="docutils literal">createdb.py</tt> script to see it in effect:</p>
<pre class="literal-block">
$ python createdb.py
Need to create database and schema
$ python createdb.py
Database exists, assume schema does, too.
$ ls
books.db
...
</pre>
<p class="incremental">Sqlite3 will automatically create a new database when you connect for the
first time, if one does not exist.</p>
</div>
<div class="section" id="set-up-a-schema">
<h1>Set Up A Schema</h1>
<p>Make the following changes to <tt class="docutils literal">createdb.py</tt>:</p>
<pre class="code python small literal-block">
<span class="n">DB_FILENAME</span> <span class="o">=</span> <span class="s">'books.db'</span>
<span class="n">SCHEMA_FILENAME</span> <span class="o">=</span> <span class="s">'ddl.sql'</span> <span class="c"># &lt;- this is new</span>
<span class="n">DB_IS_NEW</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
    <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span> <span class="c"># &lt;- context mgr</span>
        <span class="k">if</span> <span class="n">DB_IS_NEW</span><span class="p">:</span> <span class="c"># A whole new if clause:</span>
            <span class="k">print</span> <span class="s">'Creating schema'</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">SCHEMA_FILENAME</span><span class="p">,</span> <span class="s">'rt'</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">schema</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
            <span class="n">conn</span><span class="o">.</span><span class="n">executescript</span><span class="p">(</span><span class="n">schema</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">print</span> <span class="s">'Database exists, assume schema does, too.'</span>
    <span class="c"># delete the `conn.close()` that was here.</span>
</pre>
</div>
<div class="section" id="verify-your-work">
<h1>Verify Your Work</h1>
<p>Quit your python interpreter and delete the file <tt class="docutils literal">books.db</tt></p>
<div class="incremental container">
<p>Then run the script from the command line again to try it out:</p>
<pre class="literal-block">
$ python createdb.py
Creating schema
$ python createdb.py
Database exists, assume schema does, too.
</pre>
</div>
</div>
<div class="section" id="introspect-the-database">
<h1>Introspect the Database</h1>
<p>Add the following to <tt class="docutils literal">createdb.py</tt>:</p>
<pre class="code python small literal-block">
<span class="c"># in the imports, add this line:</span>
<span class="kn">from</span> <span class="nn">utils</span> <span class="kn">import</span> <span class="n">show_table_metadata</span>

<span class="k">else</span><span class="p">:</span>
    <span class="c"># in the else clause, replace the print statement with this:</span>
    <span class="k">print</span> <span class="s">&quot;Database exists, introspecting:&quot;</span>
    <span class="n">tablenames</span> <span class="o">=</span> <span class="p">[</span><span class="s">'author'</span><span class="p">,</span> <span class="s">'book'</span><span class="p">]</span>
    <span class="n">cursor</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">tablenames</span><span class="p">:</span>
        <span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span>
        <span class="n">show_table_metadata</span><span class="p">(</span><span class="n">cursor</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>
</pre>
<p class="incremental">Then try running <tt class="docutils literal">python createdb.py</tt> again</p>
</div>
<div class="section" id="my-results">
<h1>My Results</h1>
<pre class="small literal-block">
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
</pre>
</div>
<div class="section" id="inserting-data">
<h1>Inserting Data</h1>
<p>Let's load up some data. Fire up your interpreter and type:</p>
<pre class="code python small literal-block">
<span class="o">&gt;&gt;&gt;</span> <span class="kn">import</span> <span class="nn">sqlite3</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">insert</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;
... INSERT INTO author (name) VALUES(&quot;Iain M. Banks&quot;);&quot;&quot;&quot;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;books.db&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span>
<span class="o">...</span>     <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">insert</span><span class="p">)</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">rowcount</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="o">...</span>
<span class="o">&lt;</span><span class="n">sqlite3</span><span class="o">.</span><span class="n">Cursor</span> <span class="nb">object</span> <span class="n">at</span> <span class="mh">0x10046e880</span><span class="o">&gt;</span>
<span class="mi">1</span>
<span class="o">&gt;&gt;&gt;</span>
</pre>
<p class="incremental">Did that work?</p>
</div>
<div class="section" id="querying-data">
<h1>Querying Data</h1>
<p>Let's query our database to find out:</p>
<pre class="code python small literal-block">
<span class="o">&gt;&gt;&gt;</span> <span class="n">query</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;
... SELECT * from author;&quot;&quot;&quot;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;books.db&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span>
<span class="o">...</span>     <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
<span class="o">...</span>     <span class="n">rows</span> <span class="o">=</span> <span class="n">cur</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
<span class="o">...</span>     <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
<span class="o">...</span>         <span class="k">print</span> <span class="n">row</span>
<span class="o">...</span>
<span class="o">&lt;</span><span class="n">sqlite3</span><span class="o">.</span><span class="n">Cursor</span> <span class="nb">object</span> <span class="n">at</span> <span class="mh">0x10046e8f0</span><span class="o">&gt;</span>
<span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s">u'Iain M. Banks'</span><span class="p">)</span>
</pre>
<p class="incremental">Alright!  We've got data in there.  Let's make it more efficient</p>
</div>
<div class="section" id="parameterized-statements">
<h1>Parameterized Statements</h1>
<p>Try this:</p>
<pre class="code python small literal-block">
<span class="o">&gt;&gt;&gt;</span> <span class="n">insert</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;
... INSERT INTO author (name) VALUES(?);&quot;&quot;&quot;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">authors</span> <span class="o">=</span> <span class="p">[[</span><span class="s">&quot;China Mieville&quot;</span><span class="p">],</span> <span class="p">[</span><span class="s">&quot;Frank Herbert&quot;</span><span class="p">],</span>
<span class="o">...</span> <span class="p">[</span><span class="s">&quot;J.R.R. Tolkien&quot;</span><span class="p">],</span> <span class="p">[</span><span class="s">&quot;Susan Cooper&quot;</span><span class="p">],</span> <span class="p">[</span><span class="s">&quot;Madeline L'Engle&quot;</span><span class="p">]]</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;books.db&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span>
<span class="o">...</span>     <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span><span class="n">insert</span><span class="p">,</span> <span class="n">authors</span><span class="p">)</span>
<span class="o">...</span>     <span class="k">print</span> <span class="n">cur</span><span class="o">.</span><span class="n">rowcount</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="o">...</span>
<span class="o">&lt;</span><span class="n">sqlite3</span><span class="o">.</span><span class="n">Cursor</span> <span class="nb">object</span> <span class="n">at</span> <span class="mh">0x10046e8f0</span><span class="o">&gt;</span>
<span class="mi">5</span>
</pre>
</div>
<div class="section" id="check-your-work">
<h1>Check Your Work</h1>
<p>Again, query the database:</p>
<pre class="code python small literal-block">
<span class="o">&gt;&gt;&gt;</span> <span class="n">query</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;
... SELECT * from author;&quot;&quot;&quot;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;books.db&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn</span><span class="p">:</span>
<span class="o">...</span>     <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="o">...</span>     <span class="n">cur</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
<span class="o">...</span>     <span class="n">rows</span> <span class="o">=</span> <span class="n">cur</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
<span class="o">...</span>     <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
<span class="o">...</span>         <span class="k">print</span> <span class="n">row</span>
<span class="o">...</span>
<span class="o">&lt;</span><span class="n">sqlite3</span><span class="o">.</span><span class="n">Cursor</span> <span class="nb">object</span> <span class="n">at</span> <span class="mh">0x10046e8f0</span><span class="o">&gt;</span>
<span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s">u'Iain M. Banks'</span><span class="p">)</span>
<span class="o">...</span>
<span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="s">u'J.R.R. Tolkien'</span><span class="p">)</span>
<span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="s">u'Susan Cooper'</span><span class="p">)</span>
<span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="s">u&quot;Madeline L'Engle&quot;</span><span class="p">)</span>
</pre>
</div>
<div class="section" id="transactions">
<h1>Transactions</h1>
<p>Transactions group operations together, allowing you to verify them <em>before</em>
the results hit the database.</p>
<p class="incremental">In SQLite3, data-altering statements require an explicit <tt class="docutils literal">commit</tt> unless
auto-commit has been enabled.</p>
<p class="incremental">The <tt class="docutils literal">with</tt> statements we've used take care of committing when the context
manager closes.</p>
<p class="incremental">Let's change that so we can see what happens explicitly</p>
</div>
<div class="section" id="populating-the-database">
<h1>Populating the Database</h1>
<p>Let's start by seeing what happens when you try to look for newly added data
before the <tt class="docutils literal">insert</tt> transaction is committed.</p>
<p class="incremental">Begin by quitting your interpreter and deleting <tt class="docutils literal">books.db</tt>.</p>
<div class="incremental container">
<p>Then re-create the database, empty:</p>
<pre class="literal-block">
$ python createdb.py
Creating schema
</pre>
</div>
</div>
<div class="section" id="setting-up-the-test">
<h1>Setting Up the Test</h1>
<p class="small">Open <tt class="docutils literal">populatedb.py</tt> in your editor, replace the final <tt class="docutils literal">print</tt>:</p>
<pre class="code python small literal-block">
<span class="n">conn1</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span>
<span class="n">conn2</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span>
<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">On conn1, before insert:&quot;</span>
<span class="n">show_authors</span><span class="p">(</span><span class="n">conn1</span><span class="p">)</span>
<span class="n">authors</span> <span class="o">=</span> <span class="p">([</span><span class="n">author</span><span class="p">]</span> <span class="k">for</span> <span class="n">author</span> <span class="ow">in</span> <span class="n">AUTHORS_BOOKS</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
<span class="n">cur</span> <span class="o">=</span> <span class="n">conn1</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
<span class="n">cur</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span><span class="n">author_insert</span><span class="p">,</span> <span class="n">authors</span><span class="p">)</span>
<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">On conn1, after insert:&quot;</span>
<span class="n">show_authors</span><span class="p">(</span><span class="n">conn1</span><span class="p">)</span>
<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">On conn2, before commit:&quot;</span>
<span class="n">show_authors</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
<span class="n">conn1</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">On conn2, after commit:&quot;</span>
<span class="n">show_authors</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
<span class="n">conn1</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<span class="n">conn2</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre>
</div>
<div class="section" id="running-the-test">
<h1>Running the Test</h1>
<p class="small">Quit your python interpreter and run the <tt class="docutils literal">populatedb.py</tt> script:</p>
<pre class="small incremental literal-block">
On conn1, before insert:
no rows returned
On conn1, after insert:
(1, u'China Mieville')
(2, u'Frank Herbert')
(3, u'Susan Cooper')
(4, u'J.R.R. Tolkien')
(5, u&quot;Madeline L'Engle&quot;)

On conn2, before commit:
no rows returned
On conn2, after commit:
(1, u'China Mieville')
(2, u'Frank Herbert')
(3, u'Susan Cooper')
(4, u'J.R.R. Tolkien')
(5, u&quot;Madeline L'Engle&quot;)
</pre>
</div>
<div class="section" id="rollback">
<h1>Rollback</h1>
<p>That's all well and good, but what happens if an error occurs?</p>
<p class="incremental">Transactions can be rolled back in order to wipe out partially completed work.</p>
<p class="incremental">Like with commit, using <tt class="docutils literal">connect</tt> as a context manager in a <tt class="docutils literal">with</tt>
statement will automatically rollback for exceptions.</p>
<p class="incremental">Let's rewrite our populatedb script so it explicitly commits or rolls back a
transaction depending on exceptions occurring</p>
</div>
<div class="section" id="edit-populatedb-py-slide-1">
<h1>Edit populatedb.py (slide 1)</h1>
<p class="small">First, add the following function above the <tt class="docutils literal">if __name__ == '__main__'</tt>
block:</p>
<pre class="code python small literal-block">
<span class="k">def</span> <span class="nf">populate_db</span><span class="p">(</span><span class="n">conn</span><span class="p">):</span>
    <span class="n">authors</span> <span class="o">=</span> <span class="p">([</span><span class="n">author</span><span class="p">]</span> <span class="k">for</span> <span class="n">author</span> <span class="ow">in</span> <span class="n">AUTHORS_BOOKS</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
    <span class="n">cur</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
    <span class="n">cur</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span><span class="n">author_insert</span><span class="p">,</span> <span class="n">authors</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">author</span> <span class="ow">in</span> <span class="n">AUTHORS_BOOKS</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">([</span><span class="n">book</span><span class="p">,</span> <span class="n">author</span><span class="p">]</span> <span class="k">for</span> <span class="n">book</span> <span class="ow">in</span> <span class="n">AUTHORS_BOOKS</span><span class="p">[</span><span class="n">author</span><span class="p">])</span>
        <span class="n">cur</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span><span class="n">book_insert</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
</pre>
</div>
<div class="section" id="edit-populatedb-py-slide-2">
<h1>Edit populatedb.py (slide 2)</h1>
<p class="small">Then, in the runner:</p>
<pre class="code python small literal-block">
<span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn1</span><span class="p">:</span>
    <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">DB_FILENAME</span><span class="p">)</span> <span class="k">as</span> <span class="n">conn2</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">populate_db</span><span class="p">(</span><span class="n">conn1</span><span class="p">)</span>
            <span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">authors and books on conn2 before commit:&quot;</span>
            <span class="n">show_authors</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
            <span class="n">show_books</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">Error</span><span class="p">:</span>
            <span class="n">conn1</span><span class="o">.</span><span class="n">rollback</span><span class="p">()</span>
            <span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">authors and books on conn2 after rollback:&quot;</span>
            <span class="n">show_authors</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
            <span class="n">show_books</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
            <span class="k">raise</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">conn1</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
            <span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">authors and books on conn2 after commit:&quot;</span>
            <span class="n">show_authors</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
            <span class="n">show_books</span><span class="p">(</span><span class="n">conn2</span><span class="p">)</span>
</pre>
</div>
<div class="section" id="id1">
<h1>Try it Out</h1>
<p>Remove <tt class="docutils literal">books.db</tt> and recrete the database, then run our script:</p>
<pre class="small literal-block">
$ rm books.db
$ python createdb.py
Creating schema
$ python populatedb.py
</pre>
<pre class="small incremental literal-block">
authors and books on conn2 after rollback:
no rows returned
no rows returned
Traceback (most recent call last):
  File &quot;populatedb.py&quot;, line 57, in &lt;module&gt;
    populate_db(conn1)
  File &quot;populatedb.py&quot;, line 46, in populate_db
    cur.executemany(book_insert, params)
sqlite3.InterfaceError: Error binding parameter 0 - probably unsupported type.
</pre>
</div>
<div class="section" id="oooops-fix-it">
<h1>Oooops, Fix It</h1>
<p class="small">Okay, we got an error, and the transaction was rolled back correctly.</p>
<div class="incremental small container">
<p>Open <tt class="docutils literal">utils.py</tt> and find this:</p>
<pre class="code python literal-block">
<span class="s">'Susan Cooper'</span><span class="p">:</span> <span class="p">[</span><span class="s">&quot;The Dark is Rising&quot;</span><span class="p">,</span> <span class="p">[</span><span class="s">&quot;The Greenwitch&quot;</span><span class="p">]],</span>
</pre>
</div>
<div class="incremental small container">
<p>Fix it like so:</p>
<pre class="code python literal-block">
<span class="s">'Susan Cooper'</span><span class="p">:</span> <span class="p">[</span><span class="s">&quot;The Dark is Rising&quot;</span><span class="p">,</span> <span class="s">&quot;The Greenwitch&quot;</span><span class="p">],</span>
</pre>
</div>
<p class="small incremental">It appears that we were attempting to bind a list as a parameter.  Ooops.</p>
</div>
<div class="section" id="try-it-again">
<h1>Try It Again</h1>
<div class="small container">
<p>Now that the error in our data is repaired, let's try again:</p>
<pre class="literal-block">
$ python populatedb.py
</pre>
</div>
<pre class="small incremental literal-block">
Reporting authors and books on conn2 before commit:
no rows returned
no rows returned
Reporting authors and books on conn2 after commit:
(1, u'China Mieville')
(2, u'Frank Herbert')
(3, u'Susan Cooper')
(4, u'J.R.R. Tolkien')
(5, u&quot;Madeline L'Engle&quot;)
(1, u'Perdido Street Station', 1)
(2, u'The Scar', 1)
(3, u'King Rat', 1)
(4, u'Dune', 2)
(5, u&quot;Hellstrom's Hive&quot;, 2)
(6, u'The Dark is Rising', 3)
(7, u'The Greenwitch', 3)
(8, u'The Hobbit', 4)
(9, u'The Silmarillion', 4)
(10, u'A Wrinkle in Time', 5)
(11, u'A Swiftly Tilting Planet', 5)
</pre>
</div>
<div class="section" id="congratulations">
<h1>Congratulations</h1>
<p>You've just created a small database of books and authors. The transactional
protections you've used let you rest comfortable, knowing that so long as the
process completed, you've got the data you sent.</p>
<p>We'll see more of this when we build our flask app.</p>
</div>
</div>
<div class="footer">
<hr class="footer" />
<a class="reference external" href="http://github.com/cewing/training.python_web">View document source</a>.

</div>
</body>
</html>
