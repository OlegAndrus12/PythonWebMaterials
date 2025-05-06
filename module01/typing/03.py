#pip install mypy

def greet(name: str) -> str:
    return "Hello " + name

greet(123)  # This is a type error
