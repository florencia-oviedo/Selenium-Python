from pytest import mark

@mark.api
@mark.data
def test_prueba01():
    assert True

@mark.data
def test_prueba02():
    assert True

def test_prueba03():
    a = 20
    assert a <= 70



