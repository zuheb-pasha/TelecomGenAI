import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import app
import pytest

def greet_user(name: str):
    if not name:
        return "Hello, Guest! Welcome to Telecom GenAI Assistant."
    return f"Hello, {name}! Welcome to Telecom GenAI Assistant."

def test_greet_user_empty_name():
    result = app.greet_user("")
    assert result == "Hello, Guest! Welcome to Telecom GenAI Assistant."


def test_greet_user_none():
    result = app.greet_user(None)
    assert result == "Hello, Guest! Welcome to Telecom GenAI Assistant."

