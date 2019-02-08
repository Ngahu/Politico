import pytest
from app.api.v1.resources.admin_endpoints import func


def test_func():
    assert func(8) ==9





def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()