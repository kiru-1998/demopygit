import pytest

from pytestdemo.conftest import setup


@pytest.mark.usefixtures('setup')
class Testcase:

    def test_fixturedemo(self):
        print('execute test case in fixture')

    def test_fixturedemo1(self):
        print('execute test case in fixture')

    def test_fixturedemo2(self):
        print('execute test case in fixture')

    def test_fixturedemo3(self):
        print('execute test case in fixture')