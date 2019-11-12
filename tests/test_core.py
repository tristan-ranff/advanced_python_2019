import playground
import sys
import os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock


def test_find_dark_spots():
    spots = playground.core.find_peaks([(0, 4, 5), (0, 3, 3), (0, 10, 1), (0, 0, 0), (1, 1, 1)])
    assert spots == [[1, (0, 3, 3)], [3, (0, 0, 0)]]


def test_ignore_dark_spots_at_edge():
    spots = playground.core.find_peaks([(0, 0, 0), (0, 3, 3), (0, 10, 1), (0, 0, 0), (1, 1, 1)])
    assert spots == [[3, (0, 0, 0)]]
