import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client_id = ''
client_secret = ''
uname = '118412596'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

'''playlists = sp.user_playlists(uname)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
'''

uri = 'spotify:user:118412596:playlist:1lBY4hiI08LdFoIvvoixjn'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

sp_playlist = sp.user_playlist_tracks(username, playlist_id)

print sp.audio_features(['spotify:track:2myfGe1fBz9QVr7IYZXb78'])

uri_list = []
for i in sp_playlist['items']:
	uri = i['track']['uri']
	uri_list.append(uri)

feature_data = sp.audio_features(uri_list)
dflist = []

dfs = pd.read_json(json.dumps(feature_data), orient='records')
# dfs.plot(x='danceability', y='energy')
# plt.show()
dfs_1 = dfs[['danceability','energy','acousticness','instrumentalness']]


sns_plot = sns.boxplot(data=dfs_1, orient='h', palette="Set2")
fig = sns_plot.get_figure()
fig.savefig('output.svg') 


