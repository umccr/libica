.. image:: https://github.com/umccr/libiap/workflows/Pull%20Request%20Build/badge.svg
    :target: https://github.com/umccr/libiap/actions
    :alt: PR Build Status Badge

libiap
======

Python SDK/Library for IAP -- https://umccr.github.io/libiap/

TL;DR
-----

- Install through ``pip`` like so::

    pip install libiap

- Export IAP base URL and auth token::

    export IAP_BASE_URL=<baseUrl>
    export IAP_AUTH_TOKEN=<tok>

- Somewhere in your Python code::

    from libiap import libgds

    for file in libgds.list_files(volume_name='my-gds-volume-name'):
        print(file)

Development
-----------

- Setup Python virtual environment e.g. ``python -m venv venv`` and, then::

    pip install '.[test,dev]' .


- Run unit test suite::

    python -m unittest

- Or run with ``pytest``::

    pytest


- Run individual test case::

    python -m unittest tests.test_libgds.LibGDSUnitTests.test_list_files_pagination

Documentation
-------------

- Use Sphinx and reStructuredText

- Document sources are in ``sphinx/source/*.rst``

- Build doc like so::

    (cd sphinx && make clean)
    (cd sphinx && make html)

- Browse doc locally in ``sphinx/build/html/index.html``

- If all good, build for github page::

    (cd sphinx && make github)

License
-------

MIT License and DISCLAIMER

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License
