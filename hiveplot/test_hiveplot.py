from .hiveplot import get_cartesian
import numpy as np


def test_get_cartesian():
    """
    Test for get_cartesian() function.
    """
    r = 10
    theta = 23

    observed = get_cartesian(r, theta)
    actual = (r * np.sin(theta), r * np.cos(theta))

    assert np.allclose(observed[0], actual[0])
    assert np.allclose(observed[1], actual[1])
