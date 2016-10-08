import pytest

@pytest.fixture
def data_file():
    from os import path
    t = path.abspath(path.dirname(__file__))
    return path.join(t, "data/test.json")


