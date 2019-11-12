import playground


def test_find_dark_spots():
    spots = playground.core.find_peaks([(0, 4, 5), (0, 3, 3), (0, 10, 1), (0, 0, 0), (1, 1, 1)])
    assert spots == [[1, (0, 3, 3)], [3, (0, 0, 0)]]


def test_ignore_dark_spots_at_edge():
    spots = playground.core.find_peaks([(0, 0, 0), (0, 3, 3), (0, 10, 1), (0, 0, 0), (1, 1, 1)])
    assert spots == [[3, (0, 0, 0)]]