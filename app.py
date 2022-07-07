from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

CONF_URL = 'https://shib-idp-dev.dsc.umich.edu/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='oidc',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/')
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.oidc.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    token = oauth.oidc.authorize_access_token()
    user = token.get('userinfo')
    if user:
        session['user'] = user
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
