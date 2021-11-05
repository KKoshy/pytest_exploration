"""
This script is an example for pytest test methods in a test class
"""
import pytest
import random

slip_frequency_values = [(round(random.uniform(2, 3), 2), random.randint(120, 240)) for _ in range(5)]


def id_gen(val):
    if 2 <= val <= 3:
        return "slip: {}".format(val)
    if 120 <= val <= 240:
        return "frequency: {}".format(val)


class TestRearMotorSpeed:

    @pytest.mark.parametrize("slip,frequency", slip_frequency_values, ids=id_gen)
    def test_speed_limit_back_motor(self, frequency, slip, pole=4):
        slip_factor = (1 - slip / 100)
        sync_speed = 120 * frequency * slip_factor / pole
        assert sync_speed < 5950, "Speed exceeds rated speed"
