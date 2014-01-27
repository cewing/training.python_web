Steps to get a clean master branch for your git fork
====================================================

Command line instructions for getting back to a pristine master branch


1.  Make sure that you have the UWPCE repostitory set up as an additional
    remote for your local repository::

    $ git remote add uwpce git@github.com:UWPCE-PythonCert/training.python_web.git

This will give you direct access to the original copy of the repository from
the command line.

2.  Verify this worked by checking your remotes::

    $ git remote
    origin
    uwpce

Now you have *two* remote repositories connected to your local repository.

* *Origin* represents the copy of your fork of the UW PCE repository *on
  github's servers*.
* *Uwpce* is the original UW PCE repository *on github's servers*.

State the Problem
-----------------

You have a series of changes *you* have made to the *master* branch of your
repository, both the local and the *origin* remote.

Every time you make new changes for a homework and then submit a pull request,
all these old changes are included in the pull request.

State the Goal
--------------

You would like to get a *master* branch of your repository that exactly matches
the *master* branch of the UW PCE remote (*uwpce*).

Once you have this, you can then keep that branch up to date with the UW PCE
copy

And you can continue to make clean branches for each homework *starting from
that clean master*.

Steps to get there
------------------

Preserve your Old Work
++++++++++++++++++++++

First, make a branch on your local machine of your current *master*, this will
be a branch you keep that contains all your homework up until today::

    $ git branch -a
    * master
      remotes/origin/HEAD -> origin/master
      remotes/origin/gh-pages
      remotes/origin/instructor
      remotes/origin/master
      remotes/origin/week-long-format
      remotes/uwpce/master
    $ git branch keep-old-work
    $ git branch -a
    keep-old-work
    * master
      remotes/origin/HEAD -> origin/master
      remotes/origin/gh-pages
      remotes/origin/instructor
      remotes/origin/master
      remotes/origin/week-long-format
      remotes/uwpce/master

Now, you have a copy of all the work you've done to date.  It's on the
*keep-old-work* branch. You have not yet pushed this branch up to your github
account, so let's do that next, making it safe::

    $ git push -u origin keep-old-work
    Total 0 (delta 0), reused 0 (delta 0)
    To git@github.com:cewing/training.python_web.git
     * [new branch]      keep-old-work -> keep-old-work
    Branch keep-old-work set up to track remote branch keep-old-work from origin.

Okay, now there's a copy of your old work safe in a branch on *your* github
repository.

Revert Your Master
++++++++++++++++++

The next step is to *roll back your master* to a point *before you made any
changes to it*.

The key here is understanding that every change you commit to a repository in
git is associated with a *hash*, which is a big, unique identification number
you can use to refer to that specific change.  You can see these numbers when
you look at the list of commits in github.

You need to find the number of a commit by me that happened before you began
making changes.

First, open the 'commits' page on github of your fork of the class repository.

Then, scroll down until you find your first commit, which should be part of
work for session01 homework.

Then, find the last commit *before* that commit, and click on the number in the
far right of that commit listing (it should be something like `b60ea2bb70`)

This will open up that specific commit, and in the URL for that commit you will
find the full hash: `b60ea2bb7052a5bd300772d7d9d40b19b27f7a1b`.  Copy that value.

Now, we are going to reset your local *master* branch to that commit,
abandoning all the changes you (and I) have made between then and now::

    $ git branch
    keep-old-work
    * master
    $ git reset --hard b60ea2bb7052a5bd300772d7d9d40b19b27f7a1b

Now, your *local master* has been reverted to a state before you did any work.
All your changes have been deleted, but so have all the changes I've made since
the start of class.

Luckily, we can fix that.  Our next step is to fetch the *uwpce* *master*
branch, which contains all those changes I've made, but none of the changes you
made:

    $ git fetch uwpce master
    remote: Counting objects: 10, done.
    remote: Compressing objects: 100% (10/10), done.
    remote: Total 10 (delta 3), reused 7 (delta 0)
    Unpacking objects: 100% (10/10), done.
    From github.com:UWPCE-PythonCert/training.python_web
     * branch            master     -> FETCH_HEAD
       8873ba1..75a8462  master     -> uwpce/master

And finally, we can merge the changes in the *uwpce* master into our local
*master*::

    $ git branch
    keep-old-work
    * master
    $ git merge uwpce/master
    Merge made by the 'recursive' strategy.
     source/presentations/session04.rst |    7 +
     source/presentations/session06.rst | 1624 +-----------------------------------
     2 files changed, 40 insertions(+), 1591 deletions(-)


Forcibly Update
+++++++++++++++

Now, what we have is a situation where your local master has a history that is
completely different from the *origin* to which it is attached.  Your
*origin/master* still has your work on it, interleaved with the changes I've
made along the way, but your *local* master contains only my work.

If you were to try to push these changes up to *origin* (your repository) it would
fail because there's no way to reconcile the two histories.

But we don't care about the history on your *origin*, we only want to keep the
history that is represented by what is currently in your *local* master branch.
To do that, we can push with the `--force` option::

    $ git push --force origin master
    Counting objects: 25, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (11/11), done.
    Writing objects: 100% (11/11), 2.04 KiB | 0 bytes/s, done.
    Total 11 (delta 7), reused 0 (delta 0)
    To git@github.com:cewing/training.python_web.git
     + 782d17e...5fb97f3 master -> master (forced update)

Okay.  This means that now *master* both on your local machine and on the
*origin* remote (your github repository) is identical to (and up to date with)
the master in the *uwpce* repository.


Going Forward
-------------

From now on, when you want to get the very latest copies of the *uwpce*
repository, you can issue these commands::

    $ git checkout master
    $ git fetch uwpce master
    $ git merge uwpce/master
    $ git push origin master

That will fetch the changes from the *uwpce* remote *master* branch, merge them
into your *local* repository *master* branch, and then push those changes up to
your *origin* repository *master* branch.

And when you are ready to start work on a new homework assignment, you can
simply start a new branch::

    $ git checkout -b session05-homework

Once you've completed your homework, and committed all the changes to your
*local* homework branch, you can push that branch up to your *origin*
repository::

    $ git push origin session05-homework

And then, when you open a pull request for me to review your homework, you can
select your *homework branch* as the source of the pull request, and my
*master* branch as the destination. The request will contain only those changes
that are germane to your homework.

