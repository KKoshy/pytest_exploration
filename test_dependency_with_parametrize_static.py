import pytest

variants = ['40', '60', '60D', '70', '70D', '85', '85D', 'P85+', 'P85D', '90D', 'P90D', '100D', 'P100D']
# variants = ['P85D', '90D', 'P90D', '100D', 'P100D']

"""
P - ludicrous mode
D - all wheel drive
+ - 21" wheels
"""


class TestTeslaModelVariantsStatic:

    @pytest.mark.parametrize("variant", [
        pytest.param('P85D', marks=pytest.mark.dependency(name="awd01")),
        pytest.param('90D', marks=pytest.mark.dependency(name="awd02")),
        pytest.param('P90D', marks=pytest.mark.dependency(name="awd03")),
        pytest.param('100D', marks=pytest.mark.dependency(name="awd04"))
    ])
    def test_all_wheel_drive(self, variant):
        assert "D" in variant, "All Wheel Drive not supported"

    def test_performance_pack(self, variant):
        assert "+" in variant, '21" wheel not available'

    @pytest.mark.parametrize("variant", [
        pytest.param('P85D', marks=pytest.mark.dependency(name="lmod01", depends=["awd01"])),
        pytest.param('90D', marks=pytest.mark.dependency(name="lmod02", depends=["awd02"])),
        pytest.param('P90D', marks=pytest.mark.dependency(name="lmod03", depends=["awd03"])),
        pytest.param('100D', marks=pytest.mark.dependency(name="lmod04", depends=["awd04"])),
    ])
    def test_ludicrous_mode(self, variant):
        assert "P" in variant, "Ludicrous mode not enabled"

    @pytest.mark.parametrize("variant", [
        pytest.param('P85D', marks=pytest.mark.dependency(name="stability01", depends=["awd01"])),
        pytest.param('90D', marks=pytest.mark.dependency(name="stability02", depends=["awd02"])),
        pytest.param('P90D', marks=pytest.mark.dependency(name="stability03", depends=["awd03"])),
        pytest.param('100D', marks=pytest.mark.dependency(name="stability04", depends=["awd04"])),
    ])
    def test_stability(self, stage, front_trq, rear_trq, variant):
        if stage == 'acceleration':
            assert front_trq < rear_trq, "Unstable acceleration for {}".format(variant)
        if stage == 'braking':
            assert front_trq > rear_trq, "Unstable braking for {}".format(variant)
