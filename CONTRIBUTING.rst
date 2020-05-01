DEVELOPER GUIDE
===============

Clone Note
----------
* If you happen to clone this repo, recommended to keep in-sync with this repo ``master`` and ``dev`` branches as upstream.
* i.e. Make no merges in your clone on these two branches, but just keep them in-sync to avoid drift and potential conflict.


Workflow Note
-------------
* Both ``master`` and ``dev`` branches are protected with **Pull Request Build** workflow_
* Commit changes should come through pull request from a feature branch
* Run test suite and all must passed
* Merge to ``master`` create a release by practice
* Feature developer only need to focus on their feature branch get merged into ``dev`` branch
* Release maintainer evaluate ``dev`` and collate features and fixes, then merges from ``dev`` to ``master``
* Preferably, merging to ``master`` should fast-forward rebase merge to retain linear history
* If frozen or LTS release is desirable, create a release branch after its get merged into ``master`` and, keep it locked
* Bump version after every release

.. _workflow: https://github.com/umccr/libiap/actions


Feature Developer
-----------------
* Default branch is ``dev`` which you should always work towards to get merged your work
* Always start from latest ``dev`` branch e.g::

    git checkout dev
    git fetch && git pull
    git checkout -b my-feat-1
    (...work...)
    git commit -m "Write nice one or see existing commit messages for example"
    git push --set-upstream origin my-feat-1

* Create Pull Request through GitHub UI and peer review it
* If all good then merge it to ``dev``, preferably **rebase merge** with fast-forward option.
* Since GitHub `does not support committer information`_ proper, but create a new SHA upon rebase merge option, instead of clicking green button there in PR page, try like so::

    git checkout dev
    git merge --ff-only my-feat-1
    git push origin dev

* If you can not push to ``dev``, please reach out to maintainer.

.. _`does not support committer information`: https://help.github.com/en/github/administering-a-repository/about-merge-methods-on-github#rebasing-and-merging-your-commits


Release Maintainer
------------------
* Maintainer works on QA, organising and merging to ``master`` branch
* Then, deploy or upload release artifact to PyPI
* Read `Packaging Python Projects`_

.. _Packaging Python Projects: https://packaging.python.org/tutorials/packaging-projects/

Steps
^^^^^

#. Set release date (if any), rally with feature committer and, collate features/fixes
#. Probably, temporary freeze/pause PR merges into ``dev`` from feature committer at this point
#. Start a new branch, say, ``prep-release-0.1.0``
#. Finalise version number
#. Build doc and check the doc in local, then build for GitHub page ``(cd sphinx && make github)``
#. Update CHANGELOG
#. Create PR ``prep-release-0.1.0`` merge to ``dev`` branch
#. Final check and validate ``dev`` branch
#. If all good, build dist::

    python setup.py sdist bdist_wheel

#. Try TestPyPI first::

    twine upload --repository testpypi --sign dist/libiap-0.1.0*

#. Create temporary ``virtualenv`` and try::

    pip install --index-url https://test.pypi.org/simple/ --no-deps libiap
    pip list
    python
    >>> import libiap
    >>> libiap.__version__
        '0.1.0'

#. And, perform any other QA and verification tests, if any
#. If all good to this point, create a PR on GitHub, to merge ``master`` from ``dev``::

    git checkout dev
    git fetch && git pull
    git log
    git checkout master
    git merge --ff-only dev
    git push origin master

#. Upload the release to PyPI::

    twine upload --sign dist/libiap-0.1.0*

Post
^^^^
#. Tag the release commit
#. Optionally, create a release branch and locked/frozen it for LTS support, if any
#. Bump next version
#. Unfreeze or start merging PR from feature committer into ``dev``, again
#. Rinse and Spin!
