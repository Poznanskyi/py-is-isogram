from app.main import is_isogram

def test_is_isogram() -> None:
    assert is_isogram("playgrounds")
    assert not is_isogram("look")
    assert not is_isogram("Adam")
    assert is_isogram("")
    assert is_isogram("isogram")
    assert not is_isogram("GeeksforGeeks")
    assert not is_isogram("Alphabet")
    assert is_isogram("Dermatoglyphics")
