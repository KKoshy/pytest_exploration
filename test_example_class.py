"""
This script is an example for pytest test methods in a test class
"""


class TestTeslaModelTag:

    def test_roadster(self):
        assert "Roadster" == "Roadster", "Tags don't match"

    def test_model_s(self):
        assert "Model3" == "ModelS", "Tags don't match"

    def test_model_3(self):
        assert "Model3" == "Model3", "Tags don't match"

    def test_model_x(self):
        assert "ModelY" == "ModelX", "Tags don't match"

    def test_model_y(self):
        assert "ModelY" == "ModelY", "Tags don't match"
