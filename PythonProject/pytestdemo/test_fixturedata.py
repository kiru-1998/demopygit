import pytest

from pytestdemo.conftest import dataLoad


@pytest.mark.usefixtures(dataLoad)
class Data:

    def test_editprofile(self,dataLoad):

        print(dataLoad)
