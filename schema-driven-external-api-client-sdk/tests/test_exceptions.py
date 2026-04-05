
from exceptions import APIContractError, NetworkError, SDKError


def test_APIContractError():
    api_err = APIContractError("Invalid Response", {"Id": 99}, {"type": "object"})

    network_err = NetworkError("Internal Server Error", 500)

    assert api_err.message == "Invalid Response"
    assert api_err.received_data == {"Id": 99}
    assert api_err.expected_schema == {"type": "object"}


    assert isinstance(api_err, SDKError)

    assert network_err.message == "Internal Server Error"
    assert network_err.status_code == 500
