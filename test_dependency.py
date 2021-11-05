import pytest

MODEL_S_VARIANT = '90D'


class TestTeslaModelS90D:

    @pytest.mark.dependency()
    def test_all_wheel_drive(self):
        assert "D" in MODEL_S_VARIANT, "All Wheel Drive not supported"

    def test_performance_pack(self):
        assert "+" in MODEL_S_VARIANT, '21" wheel not available'

    @pytest.mark.dependency(depends=["TestTeslaModelS90D::test_all_wheel_drive"])
    def test_ludicrous_mode(self):
        assert "P" in MODEL_S_VARIANT, "Ludicrous mode not enabled"

    @pytest.mark.dependency(depends=["TestTeslaModelS90D::test_all_wheel_drive"])
    def test_stability(self, stage, front_trq, rear_trq):
        if stage == 'acceleration':
            assert front_trq < rear_trq, "Unstable acceleration"
        if stage == 'braking':
            assert front_trq > rear_trq, "Unstable braking"
