import pytubepubsub as pyt
from unittest.mock import patch

channel_id = "UCSHZKyawb77ixDdsGog4iWA"
callback_url = "http://localhost:8080/callback"


def mocked_request_get_post(url, headers=None, data=None):
    class MockedResponse:
        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text

        def json(self):
            return self.text

    return MockedResponse(200, {"status": "ok"})


@patch("requests.post", side_effect=mocked_request_get_post)
def test_create(mocked_request):
    lease = pyt.create(channel_id, callback_url)
    assert lease.response.status_code == 200
    assert mocked_request.call_count == 1
    assert mocked_request.called_with(
        "https://pubsubhubbub.appspot.com/subscribe",
    )
