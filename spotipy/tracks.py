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
start = time.time()

for index, row in songs_array.iterrows():
	track_name = (row['songs'])
	results = sp.search(q=track_name, limit=1)
	tids = []

	if not results['tracks']['items']:
		song_name = track_name
		jsonDict[index] = [song_name, '', '', '', '', '', '', '', '']
		print (song_name)
	
	else:
		for i, t in enumerate(results['tracks']['items']):
			
			#print(' ', i, t['name'], t['artists'], t['popularity'])
			tids.append(t['uri'])
			
			#define each varialbe needed from the "search for an item" query for the project
			song_name = t['name']
			popularity = t['popularity']
			artists = t['artists']		
		
		features = sp.audio_features(tids)
		
		#define each variable needed from the "get audio features" query for the project
		energy = features[0]['energy']
		dance = features[0]['danceability']
		liveness = features[0]['liveness']
		valence = features[0]['valence']
		tempo = features[0]['tempo']
		instrumental = features[0]['instrumentalness']
		acoustic = features[0]['acousticness']
		jsonDict[index] = [song_name, energy, dance, liveness, valence, tempo, instrumental, acoustic, popularity]
		print(json.dumps(features, indent=4))

df = pd.DataFrame(jsonDict).T
df.columns = ['song', 'energy', 'dance', 'liveness', 'valence', 'tempo', 'instrumental', 'acoustic', 'popularity']
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
delta = time.time() - start
print ("features retrieved in %.2f seconds" % (delta,))

#text to column, separated by commas (within excel)


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