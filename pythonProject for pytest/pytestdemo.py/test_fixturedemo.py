import pytest


@pytest.mark.usefixtures('setup')
class Testcase:

    def test_fixtureDemo(self):
        print('i will be execute test cases in fixture')

    def test_fixtureDemo1(self):
        print('i will be execute test cases in fixture')

    def test_fixtureDemo2(self):
        print('i will be execute test cases in fixture')

    def test_fixtureDemo3(self):
        print('i will be execute test cases in fixture')