import pytest
#method name should have sense

@pytest.mark.skip
def test_firstProgram():
    msg = 'hello'
    assert msg == 'hi' #test case failed due to strings do not match


def test_secondCreditcard(setup):

    a=2
    b=6
    assert a+4==6 #addition donot match







