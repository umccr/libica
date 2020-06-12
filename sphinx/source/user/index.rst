USER GUIDE
==========

OpenAPI
-------

* For usage of sub-packages (e.g. ``libiap.openapi.libwes``), please refer to OpenAPI documentation available at:

    `https://umccr-illumina.github.io/libiap/openapi/ <https://umccr-illumina.github.io/libiap/openapi/>`_

Basic
-----

* Generally, it is straight forward use. Each `sub-modules <../libiap>`_ backing respective IAP web services. And each module's function map to API HTTP method calls. Query parameters can be pass as keyword arguments into function. Module function return dictionary-backed object which is directly deserialized from API JSON response.

* By default, ``libiap`` look into environment variables for ``IAP_BASE_URL`` and ``IAP_AUTH_TOKEN``. If you set these, they will be used for forming base URL for endpoint and authentication bearer token.

* You may also set base URL and auth token as keyword arguments during function call as follow. However, environment variables take precedence::

    from libiap import libgds

    url = 'https://use1.platform.illumina.com'
    token = '<tok>'

    for file in libgds.list_files(volume_name='volume-name', iap_base_url=url, iap_auth_token=token):
        print(file)

* All ``list_*`` function calls are paginated with default page size ``1000``. You may overwrite this as::

    for file in libgds.list_files(volume_name='volume-name', page_size=10):
        print(file)

* All ``list_*`` functions implementations are backed by Python generator. Therefore, you will need to iterate through it. Example, this check won't work::

    if len(libgds.list_files(volume_name='volume-name')) > 10:
        print("won't reach here")

* To pick just one, wrap ``next(..)``::

    file = next(libgds.list_files(volume_name='volume-name'))


REST Client
-----------

* You may also directly utilise ``rest`` module and its client implementation.

* First, build REST ``Client`` as follows::

    from libiap import rest
    from libiap.rest import Client

    ep = 'https://use1.platform.illumina.com/v1/health'

    client: Client = rest.build(ep)
    health = client.get()


Example ``pilot.py``
--------------------

.. literalinclude:: ../../../pilot.py
