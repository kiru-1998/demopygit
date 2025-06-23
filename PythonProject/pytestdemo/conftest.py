import pytest


@pytest.fixture(scope='class')
def setup():
    print('execute first')
    yield
    print('execute last')


@pytest.fixture()
def dataLoad():
    print('user profile created succesfully')
    return['rahul','shetty','rahulshettyacademy']