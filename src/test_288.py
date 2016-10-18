"""Testing for dailyprogramer challenge #288."""


def test_include():
    """Test if module can be imported."""
    from dp288 import alliteration


def test_return_string():
    """Test for a sting value returned."""
    from dp288 import alliteration
    return_value = alliteration()
    assert(isinstance(return_value, (str)))
