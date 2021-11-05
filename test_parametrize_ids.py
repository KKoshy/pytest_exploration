"""
This script is an example for pytest test methods in a test class
"""
import pytest
import random

slip_frequency_values = [(round(random.uniform(2, 3), 2), random.randint(120, 240)) for _ in range(5)]


class TestFrontMotorSpeed:

    # Five ids are given because there are five sets of test data
    @pytest.mark.parametrize("slip, frequency", slip_frequency_values, ids=['state1', 'state2', 'state3', 'state4',
                                                                            'state5'])
    def test_speed_limit_front_motor(self, frequency, slip, pole=4):
        slip_factor = (1 - slip / 100)
        pytest.set_trace()
        sync_speed = 120 * frequency * slip_factor / pole
        assert sync_speed < 6100, "Speed exceeds rated speed"
