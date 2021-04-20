def search4letters(phrase, letters):
    # return set(letters).intersection(set(phrase))
    intersection = set(letters).intersection(set(phrase))
    if intersection == set():
        return "Empty result"
    else:
        return intersection
