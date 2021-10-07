# PytubePubsub

A Python package for making subscriptions to YouTube's pubsubhubbub
service simple!

## Installation

```shell
$ git clone git@github.com:Ecalzo/pytubepubsub.git
$ python3 setup.py install
```

```python
import pytubepubsub as pyt

yt_channel_id = "UCSHZKyawb77ixDdsGog4iWA"
callback_url = "https://my-website/callback_url"

lease = pyt.create(yt_channel_id, callback_url)
lease.health_check()

response_details = lease.get_response()

pyt.renew_lease(yt_channel_id, callback_url)
```
