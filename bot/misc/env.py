# Importing necessary components for the Env class
import os
from abc import ABC
from typing import Final


# Abstract base class for handling environment variables
class Env(ABC):
    """
    An abstract base class for handling environment variables in the application.

    Attributes:
    - TOKEN (str): A constant representing the token used for authentication.
      The value is fetched from the 'TOKEN' environment variable, or a default value ('define me!')
      is used if the environment variable is not set.
    """
    TOKEN: Final = os.environ.get('TOKEN', 'define me!')
