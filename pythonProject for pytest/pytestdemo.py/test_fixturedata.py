import pytest


@pytest.mark.usefixtures('dataLoad')
class Test:

    def test_editProfile(self,dataLoad):

        print(dataLoad)