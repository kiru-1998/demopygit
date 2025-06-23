import pytest


@pytest.mark.skip
def test_fun():
    msg= 'Hi'
    assert msg == 'hello'

def test_add():
    a=4
    b=6
    assert a+2==6



