## Global Hack 7 Repository


### Steps to Run
* create/activate new python env(3.x)
* pip install -r requirements.txt
* `python main.py`

Your API should be accessible locally.

### GCP Deployment:
* install gcloud cli and setup project on GCP console
* `gcloud app deploy`

Your API should be accessible on cloud.

### Required JSON, Keys and Ciphers:

* twilio.json
```
{
  "account_sid": "account_sid",
  "auth_token": "auth_token"
}
```
* twitter.json
```
{
  "consumer_key": "consumer_key",
  "consumer_secret": "consumer_secret",
  "access_token": "access_token",
  "access_token_secret": "access_token_secret"
}
```
* cipher_key.txt(add a cipher text)
* service.json(Firebase config json)

