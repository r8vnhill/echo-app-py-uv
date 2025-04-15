"""
Simple command-line interface for the echo utility.

This script reads command-line arguments and echoes each one using the `echo` function from the
`echo_core` module. It is designed to demonstrate basic usage of argument parsing and modular
function calls in Python.

## Example:
```sh
python -m echo_app.main "There was a HOLE here." "It's gone now."
# Output:
# There was a HOLE here.
# It's gone now.
```
"""

from echo_core import echo

def main(args: list[str]):
    """
    Echoes each string in the provided list of arguments.

    Args:
        args (list[str]): List of strings to be echoed to standard output.
    """
    for arg in args:
        print(echo(arg))


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
