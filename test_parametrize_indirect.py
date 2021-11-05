"""
This script is an example for pytest test methods in a test class
"""
import pytest
import random

POLE = 4
slip_frequency_values = [(round(random.uniform(2, 3), 2), random.randint(120, 240)) for _ in range(5)]


@pytest.fixture(scope="session")
def slip_factor(request):
    return 1 - request.param / 100


@pytest.fixture(scope="session")
def sync_speed_factor(request):
    return 120 * request.param / POLE


class TestRearMotorSpeed:

    @pytest.mark.parametrize("slip_factor,sync_speed_factor", slip_frequency_values,
                             indirect=['slip_factor', 'sync_speed_factor'])
    def test_speed_limit_back_motor(self, slip_factor, sync_speed_factor):
        sync_speed = slip_factor * sync_speed_factor
        assert sync_speed < 5950, "Speed exceeds rated speed"
