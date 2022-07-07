# flask-authlib-oidc

Sample Flask app implementing OIDC login using authlib

This seems to want client_secret_basic

This is relevant - https://docs.authlib.org/en/latest/client/flask.html
Whatever name is used to register the client (in this case "oidc")..
```
oauth.register(
    name='oidc',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)
```
is used to supply the client_id and client_secret, e.g.
```
OIDC_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')
OIDC_CLIENT_SECRET = os.getenv('OIDC_CLIENT_SECRET')
```
