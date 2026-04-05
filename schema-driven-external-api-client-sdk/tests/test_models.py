import pytest

from models import User

def test_instantiate_user():
    user = User(1, "Joshua", "test@gmail.com", True)

    with pytest.raises(AttributeError):
        fakedict = user.__dict__

    with pytest.raises(AttributeError):
        user.is_admin = True
