from seamtilt.core import calculate_tilt

def test_calculate_tilt():
    assert calculate_tilt(10, 20) == 5.0
    assert calculate_tilt(-10, 10) == 10.0
