from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

songs_array = pd.read_excel('songs.xlsx')
print(songs_array)

jsonDict = {}
song_name = ''

for index, row in songs_array.iterrows():
	track_name = (row['songs'])
	results = sp.search(q=track_name, limit=1)
	tids = []
	for i, t in enumerate(results['tracks']['items']):
		print(' ', i, t['name'])
		tids.append(t['uri'])
		song_name = t['name']
	
	start = time.time()
	features = sp.audio_features(tids)
	jsonDict[index] = [song_name, features]
	delta = time.time() - start
	print(json.dumps(features, indent=4))
	print ("features retrieved in %.2f seconds" % (delta,))
df = pd.DataFrame(jsonDict).T
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# if len(sys.argv) > 1:
#     track_name = ''.join(sys.argv[1:])
#     results = sp.search(q=track_name, limit=1)
#     tids = [""]
#     for i, t in enumerate(results['tracks']['items']):
#         print(' ', i, t['name'])
#         tids.append(t['uri'])

#     start = time.time()
#     features = sp.audio_features(tids)
#     delta = time.time() - start
#     print(json.dumps(features, indent=4))
#     print ("features retrieved in %.2f seconds" % (delta,)) 