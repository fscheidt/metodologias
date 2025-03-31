import pytest
from src.area.square import square_area

def test_square_area_string_args():
    with pytest.raises(Exception):
        assert square_area("a2")
