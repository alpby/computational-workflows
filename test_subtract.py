import pytest
from subtract import subtract
import numpy as np

def test_subtracting():
  c = subtract(30,20)
  assert(c == 10)

def test_subtracting_float():
  c = subtract(50.0,30.0)
  assert(np.isclose(c, 20.0))

@pytest.mark.parametrize("a,b,result", [(3,5,-2), (3,4,-1), (10,-3, 13)])
def test_subtract_param(a,b,result):
  c = subtract(a,b)
  assert(c == result)

def test_subtract_error():
  with pytest.raises(TypeError):
    c = subtract(3, "4")


