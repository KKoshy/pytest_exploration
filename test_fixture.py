import pytest
import random


@pytest.fixture(scope='module')
def slip():
    return round(random.uniform(2, 3), 2)


@pytest.fixture(scope='module')
def frequency():
    return random.randint(120, 240)


class TestCurrentSpeed:
    def test_current_speed(self, slip, frequency, pole=4):
        slip_factor = (1 - slip / 100)
        sync_speed = 120 * frequency * slip_factor / pole
        assert sync_speed < 6100, "Speed exceeds rated speed"
