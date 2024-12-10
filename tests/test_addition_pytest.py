import pytest
from app import add  # Assuming your function is in app.py

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, 200) == 300
