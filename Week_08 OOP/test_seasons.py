from seasons import minutes_lived

def test_invalid():
    assert minutes_lived(2020, 25, 27) == "Invalid date"
    assert minutes_lived(2020, 7, 40) == "Invalid date"


def test_valid():
    assert minutes_lived(2020,7,4) == "Two million, two hundred sixty-two thousand, two hundred forty minutes"
    assert minutes_lived(2024,10,21) == "One thousand, four hundred forty minutes"
