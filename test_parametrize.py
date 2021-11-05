"""
This script is an example for pytest test methods in a test class
"""
import pytest

torque_values = [('acceleration', 400, 250), ('braking', 300, 500), ('acceleration', 330, 400), ('braking', 445, 350)]


class TestMotorStats:

    @pytest.mark.parametrize("stage, front_trq, rear_trq", torque_values)
    def test_stability(self, stage, front_trq, rear_trq):
        if stage == 'acceleration':
            assert front_trq < rear_trq, "Unstable acceleration"
        if stage == 'braking':
            assert front_trq > rear_trq, "Unstable braking"

