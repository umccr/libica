__version__ = VERSION = '0.4.0rc1'

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

__alpha_deprecation__ = "Module or function may be deprecated in future. " \
                        "Please use libiap.openapi when possible for better upstream support."
