from app.main import is_isogram

def test_is_isogram() -> None:
    assert is_isogram("playgrounds")
    assert not is_isogram("look")
    assert not is_isogram("Adam")
    assert is_isogram("")
