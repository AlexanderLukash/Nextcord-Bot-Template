# Importing necessary components for the Config class
from abc import ABC
from typing import Final


# Abstract base class for configuration settings
class Config(ABC):
    """
    An abstract base class for managing application configuration settings.

    Attributes:
    - CMD_PREFIX (str): A constant representing the command prefix used in the application.
      This can be customized according to the needs of the bot or application.
    """
    CMD_PREFIX: Final = '/'
