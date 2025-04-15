# echo-app-py-uv

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![uv](https://img.shields.io/badge/built%20with-uv-6c6cff?logo=python)
![License: BSD-2](https://img.shields.io/badge/license-BSD--2--Clause-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey)
[![View lesson (ES)](https://img.shields.io/badge/ver%20lecci%C3%B3n-inicial-blueviolet)](https://dibs.pages.dev/docs/build-systems/init/uv)
[![View lesson (ES)](https://img.shields.io/badge/ver%20lecci%C3%B3n-modular-blueviolet)](https://dibs.pages.dev/docs/build-systems/modular-design/uv)

This repository accompanies two lessons on building modern Python projects using [`uv`](https://docs.astral.sh/uv/), a fast and user-friendly tool for managing virtual environments and dependencies via `pyproject.toml`.

> 📘 The lessons are written in Spanish and can be found at:
>
> - [Lesson 1 – Basic setup](https://dibs.pages.dev/docs/build-systems/init/uv)
> - [Lesson 2 – Modular structure](https://dibs.pages.dev/docs/build-systems/modular-design/uv)
>
> However, the code and repository are written in English to ensure broader accessibility.

## 🧱 Project structure

This project follows a modular design using `uv workspaces`, separating business logic (`core`) from the application layer (`app`).

```
.
├── core
│   ├── echo_core
│   │   ├── __init__.py
│   │   └── echo.py
│   └── pyproject.toml
├── app
│   ├── echo_app
│   │   ├── __init__.py
│   │   └── main.py
│   └── pyproject.toml
├── pyproject.toml
├── uv.lock
└── README.md
```

## ▶️ How to run it

From the root directory, you can execute the application like this:

```bash
uv run app/echo_app/main.py Butcher Hughie Kimiko Frenchie M.M.
```

Expected output:

```text
Butcher
Hughie
Kimiko
Frenchie
M.M.
```

## 💡 What's inside?

The `core` module contains a reusable function:

```python
# core/echo_core/echo.py
def echo(message: str) -> str:
    return message
```

The `app` module consumes it:

```python
# app/echo_app/main.py
from echo_core import echo

def main(args: list[str]):
    for arg in args:
        print(echo(arg))

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
```

## 📖 Learn more

These lessons guide you from a simple script to a **modular and scalable project structure**, preparing you for more advanced topics like testing, packaging, and CI.

- [Lesson 1 – Basic setup](https://dibs.pages.dev/docs/build-systems/init/uv)
- [Lesson 2 – Modular structure](https://dibs.pages.dev/docs/build-systems/modular-design/uv)

## 🔗 Resources

- [Official uv documentation – "Using workspaces"](https://docs.astral.sh/uv/concepts/projects/workspaces/)
- [Official uv documentation – "Working on projects"](https://docs.astral.sh/uv/guides/projects/)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
