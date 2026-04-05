import json
import pytest
from unittest.mock import patch, MagicMock
from client import APIClient
from exceptions import APIContractError, NetworkError

URL = "https://fakeapi.com/users"

def make_mock_response(data: list):
    """Helper to build a fake urlopen context manager response."""
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(data).encode("utf-8")
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)
    return mock_response


# ── Happy path ────────────────────────────────────────────────────────────────

@patch("client.urllib.request.urlopen")
def test_fetch_users_returns_user_objects(mock_urlopen):
    fake_data = [
        {"id": 1, "username": "john", "email": "john@yahoo.com", "is_active": True},
        {"id": 2, "username": "jane", "email": "jane@gmail.com", "is_active": False},
    ]
    mock_urlopen.return_value = make_mock_response(fake_data)

    client = APIClient()
    users = client.fetch_users(URL)

    assert len(users) == 2
    assert users[0].username == "john"
    assert users[1].username == "jane"


@patch("client.urllib.request.urlopen")
def test_fetch_users_calls_correct_url(mock_urlopen):
    mock_urlopen.return_value = make_mock_response([])

    APIClient().fetch_users(URL)

    mock_urlopen.assert_called_once_with(URL)


# ── Contract errors ───────────────────────────────────────────────────────────

@patch("client.urllib.request.urlopen")
def test_fetch_users_missing_field_raises_api_contract_error(mock_urlopen):
    fake_data = [
        {"id": 1, "username": "john"}  # missing email and is_active
    ]
    mock_urlopen.return_value = make_mock_response(fake_data)

    with pytest.raises(APIContractError):
        APIClient().fetch_users(URL)


# ── Network errors ────────────────────────────────────────────────────────────

@patch("client.urllib.request.urlopen")
def test_fetch_users_raises_network_error_on_failure(mock_urlopen):
    mock_urlopen.side_effect = NetworkError("Internal Server Error", 500)

    with pytest.raises(NetworkError) as exc_info:
        APIClient().fetch_users(URL)

    assert exc_info.value.status_code == 500
