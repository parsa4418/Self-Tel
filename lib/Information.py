from .library import *
import os

admin_user_id = int(os.environ['ADMIN_USER_ID'])
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
helper_username = os.environ['HELPER_USERNAME']
bot_token = os.environ['BOT_TOKEN']

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']


import os


client = TelegramClient('main_session', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
