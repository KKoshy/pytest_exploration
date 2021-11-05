"""
This script is an example for pytest test functions format
"""


def test_roadster():
    assert "Roadster" == "Roadster", "Tags don't match"


def test_model_s():
    assert "Model3" == "ModelS", "Tags don't match"


def test_model_3():
    assert "Model3" == "Model3", "Tags don't match"


def _test_model_x():
    assert "ModelY" == "ModelX", "Tags don't match"


def test_model_y():
    assert "ModelY" == "ModelY", "Tags don't match"
