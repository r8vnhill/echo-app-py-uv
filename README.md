# echo-app-py-uv

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![uv](https://img.shields.io/badge/built%20with-uv-6c6cff?logo=python)
![License: BSD-2](https://img.shields.io/badge/license-BSD--2--Clause-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey)
[![View lesson (ES)](https://img.shields.io/badge/ver%20lección-en%20español-blueviolet)](https://dibs.pages.dev/docs/build-systems/init/uv)

This repository contains the initial setup for a modern Python project using [`uv`](https://docs.astral.sh/uv/), a fast and user-friendly tool for managing virtual environments and dependencies via `pyproject.toml`.

> 📘 The accompanying lesson is written in Spanish and can be found at:  
> [https://dibs.pages.dev/docs/build-systems/init/uv](https://dibs.pages.dev/docs/build-systems/init/uv)  
> However, the code and repository are written in English to ensure broader accessibility.

## 🧱 Project structure

This repository was initialized using:

```bash
uv init
```

As a result, it includes the following structure:

```
.
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
└── README.md
```

## ▶️ How to run it

Create and activate a virtual environment, then run the app:

### On Linux/macOS

```bash
uv venv && \
source .venv/bin/activate && \
python main.py
```

Or simply:

```bash
uv run main.py
```

### On Windows (PowerShell)

```powershell
uv venv; `
.\.venv\Scripts\Activate.ps1; `
py main.py
```

Or:

```powershell
uv run main.py
```

## 💡 What's inside?

The file `main.py` contains a simple hello world program inspired by Foo Fighters:

```python
def main():
    print("It's times like these you learn to code again.")

if __name__ == "__main__":
    main()
```

## 📖 Learn more

This project is meant to be a stepping stone toward scalable, modular, and maintainable Python projects — including multiple modules, testing, packaging, and more.

If you're comfortable with Spanish, check out the full lesson for a step-by-step explanation:
[https://dibs.pages.dev/docs/build-systems/init/uv](https://dibs.pages.dev/docs/build-systems/init/uv)

## 🔗 Resources

- [Official uv documentation – "Working on projects"](https://docs.astral.sh/uv/guides/projects/)
- [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
