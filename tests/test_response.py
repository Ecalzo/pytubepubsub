from pytubepubsub.response import PubsubResponse
from unittest.mock import patch
import pytest

channel_id = "UCSHZKyawb77ixDdsGog4iWA"
callback_url = "http://localhost:8080/callback"


class MockedResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = str(text)

    def json(self):
        return self.text


def mocked_request_post(url, headers=None, data=None):
    return MockedResponse(200, {"status": "ok"})


def mocked_request_get(url, headers=None, data=None, params=None):
    return MockedResponse(200, {"status": "ok"})


def mocked_request_get_fail(url, headers=None, data=None, params=None):
    return MockedResponse(500, {"status": "unverified"})


@patch("requests.get", side_effect=mocked_request_get)
def test_pubsub_response(mocked_request_get):
    response = PubsubResponse(
        channel_id, callback_url, MockedResponse(200, {"status": "ok"}))

    assert response.health_check() is True
    assert response.get_response().status_code == 200


@patch("requests.get", side_effect=mocked_request_get_fail)
def test_pubsub_response_fail(mocked_request_get_fail):
    with pytest.raises(Exception) as err_info:
        fail_response = PubsubResponse(
            channel_id, callback_url, MockedResponse(200, {"status": "ok"}))
        fail_response.health_check()

    assert channel_id in str(err_info.value)
    assert callback_url in str(err_info.value)
