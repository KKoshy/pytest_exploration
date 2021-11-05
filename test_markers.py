import pytest

model_s = {'top_accerl': 3.1, 'awd': True, 'top_speed': 155, 'power': 670}
model_3 = {'top_accerl': 4.2, 'awd': True, 'top_speed': 145, 'power': 346}


class TestModelSpecs:

    @pytest.mark.model_3
    def test_acceleration_3(self):
        assert model_3['top_accerl'] < 5, 'Acceleration takes more than 5 seconds'

    @pytest.mark.model_s
    def test_acceleration_s(self):
        assert model_s['top_accerl'] < 5, 'Acceleration takes more than 5 seconds'

    @pytest.mark.model_3
    def test_awd_3(self):
        assert model_3['awd'], 'All Wheel Drive not enabled'

    @pytest.mark.model_s
    def test_awd_s(self):
        assert model_s['awd'], 'All Wheel Drive not enabled'

    @pytest.mark.model_3
    def test_speed_3(self):
        assert model_3['top_speed'] >= 150, 'Top speed is less than 150 mph'

    @pytest.mark.model_s
    def test_speed_s(self):
        assert model_s['top_speed'] >= 150, 'Top speed is less than 150 mph'
