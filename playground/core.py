def find_peaks(list_of_entities):
    # Find peaks
    # Find local maxima for a given list of intensities. Intensities are defined as local maxima if the intensities
    # of the elemetns in the list before and after are smaller than the peak we want to determine.
    # Args: list of floats or ints
    max_value = 0
    list_of_dark_spots = []
    for pos, element in enumerate(list_of_entities):
        if pos == 0:
            continue
        if pos == len(list_of_entities) - 1:
            continue
        if sum(list_of_entities[pos - 1]) > sum(element) < sum(list_of_entities[pos + 1]):
            list_of_dark_spots.append([pos, element])

    return list_of_dark_spots
