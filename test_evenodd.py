from even_odd import check_even_odd

def test_even():
    assert check_even_odd(4) == "Even"

def test_odd():
    assert check_even_odd(7) == "Odd"

def test_zero():
    assert check_even_odd(0) == "Even"
