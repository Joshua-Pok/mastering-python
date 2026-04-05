from typing import override

class SDKError(Exception):

    @override
    def __init__(self, message, received_data, expected_schema):
        super().__init__(message)
        self.message = message
        self.received_data = received_data
        self.expected_schema = expected_schema


class APIContractError(SDKError):

    @override
    def __init__(self, message, received_data, expected_schema):
        super().__init__(message, received_data, expected_schema)


class NetworkError(SDKError):

    @override
    def __init__(self, message, status_code = None):
        super().__init__(message = message, received_data=None, expected_schema=None)
        self.message = message
        self.status_code = status_code

