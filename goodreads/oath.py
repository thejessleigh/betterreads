from rauth.service import OAuth1Service, OAuth1Session
# Get a real consumer key & secret from: http://www.goodreads.com/api/keys
key = '<API_KEY>'
secret = '<API_SECRET>'

goodreads = OAuth1Service(
    consumer_key=key,
    consumer_secret=secret,
    name='goodreads',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    base_url='http://www.goodreads.com/'
    )

# head_auth=True is important here; this doesn't work with oauth2 for some reason
request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

authorize_url = goodreads.get_authorize_url(request_token)
print('Visit this URL in your browser: ' + authorize_url)
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = input('Have you authorized me? (y/n) ')

session = goodreads.get_auth_session(request_token, request_token_secret)

# these values are what you need to save for subsequent access.
oauth_access_token = session.access_token
oauth_access_token_secret = session.access_token_secret
print(oauth_access_token)
print(oauth_access_token_secret)
