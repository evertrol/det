"""
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from .base import *
from .local import *

try:
    from .drf import *
except ImportError:
    pass
try:
    from .graphene import *
except ImportError:
    pass

# Add any extra settings not suitable in base or another specific
# settings module in `extra.py`
try:
    from .extra import *
except ModuleNotFoundError:
    pass
