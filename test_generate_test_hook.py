class TestTeslaModelVariantHook:

    def test_all_wheel_drive(self, variant):
        assert "D" in variant, "All Wheel Drive not supported"

    def test_performance_pack(self, variant):
        assert "+" in variant, '21" wheel not available'
