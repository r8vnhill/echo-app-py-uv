"""
Core functionality for echoing messages.

This module provides a minimal utility function that returns any input string unchanged. It serves
as a foundation for demonstration, testing, or educational purposes in simple command-line or
modular Python applications.
"""


def echo(message: str) -> str:
    """
    Returns the input message unchanged.

    ## Examples:

    >>> echo("There was a HOLE here. It's gone now.")
    # Output: 'There was a HOLE here. It's gone now.'

    Args:
        message (str): The message to echo.

    Returns:
        str: The same message that was passed in.
    """
    return message
