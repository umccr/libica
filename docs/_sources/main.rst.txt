.. private repo, failing status badge image loading, commented out for now
.. .. image:: https://github.com/umccr-illumina/libiap/workflows/Pull%20Request%20Build/badge.svg
    :target: https://github.com/umccr-illumina/libiap/actions
    :alt: PR Build Status Badge

libiap
======

Python SDK/Library for IAP -- https://umccr-illumina.github.io/libiap/

* Documentation as of libiap-|release|
* `Test Coverage <https://umccr-illumina.github.io/libiap/coverage/>`_
* `PyDoc <https://umccr-illumina.github.io/libiap/libiap/>`_

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

- More examples/tutorials available at `User Guide <https://umccr-illumina.github.io/libiap/user/>`_

Development
-----------

- Pilot run or Integration Test::

    export IAP_BASE_URL=<baseUrl>
    export IAP_AUTH_TOKEN=<tok>
    python pilot.py

- See `Developer Guide <https://umccr-illumina.github.io/libiap/developer/>`_ for more notes


License
-------

MIT License and DISCLAIMER

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License
