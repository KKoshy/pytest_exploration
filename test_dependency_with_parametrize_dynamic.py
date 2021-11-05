import pytest

# variants = ['40', '60', '60D', '70', '70D', '85', '85D', 'P85+', 'P85D', '90D', 'P90D', '100D', 'P100D']
variants = ['P85D', '90D', 'P90D', '100D', 'P100D']

"""
P - ludicrous mode
D - all wheel drive
+ - 21" wheels
"""


def variant_id(case, depend_case=None):
    case_id, count = [], 0
    if not depend_case:
        for variant in variants:
            case_id.append(pytest.param(variant,
                                        marks=pytest.mark.dependency(name=case + str(count))))
            count += 1
    else:
        for variant in variants:
            case_id.append(pytest.param(variant,
                                        marks=pytest.mark.dependency(name=case + str(count),
                                                                     depends=[depend_case +
                                                                              str(count)])))
    return case_id


class TestTeslaModelVariantsDynamic:

    @pytest.mark.parametrize("variant", variant_id("awd"))
    def test_all_wheel_drive(self, variant):
        assert "D" in variant, "All Wheel Drive not supported"

    @pytest.mark.parametrize("variant", variant_id("perf_pack"))
    def test_performance_pack(self, variant):
        assert "+" in variant, '21" wheel not available'

    @pytest.mark.parametrize("variant", variant_id("lmode", "awd"))
    def test_ludicrous_mode(self, variant):
        assert "P" in variant, "Ludicrous mode not enabled"

    @pytest.mark.parametrize("variant", variant_id("stablity", "awd"))
    def test_stability(self, stage, front_trq, rear_trq, variant):
        if stage == 'acceleration':
            assert front_trq < rear_trq, "Unstable acceleration for {}".format(variant)
        if stage == 'braking':
            assert front_trq > rear_trq, "Unstable braking for {}".format(variant)
