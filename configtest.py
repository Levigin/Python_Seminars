import pytest
from checkers import writer


@pytest.fixture()
def data_record():
    return writer()
