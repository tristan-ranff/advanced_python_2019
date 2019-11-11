import pytest
import sys, os

import playground


def test_find_peaks():
    peaks = playground.core.find_peaks([(0, 4, 5), (0, 3, 3), (0, 10, 1), (0, 0, 0), (1, 1, 1)])
    assert peaks == [1, 3]