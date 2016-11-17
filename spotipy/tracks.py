from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd

#setting up Spotify credentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

#read and output the inputted excel sheet
songs_array = pd.read_excel('songs.xlsx')
print(songs_array)

jsonDict = {}
song_name = ''
start = time.time()

#Go through each song in the song column (index corresponds with the row, row = track name in that row)
for index, row in songs_array.iterrows():
	track_name = (row['songs'])

	#search for a song named 'track_name' in Spotify
	results = sp.search(q=track_name, limit=1)
	tids = []

	#if no song was found in Spotify, output the song name that was read in and empty fields
	if not results['tracks']['items']:
		song_name = track_name
		jsonDict[index] = [song_name, '', '', '', '', '', '', '', '', '', '']
		print (song_name)
	
	#if song was found on Spotify
	else:

		#Find the track's ID to get audio features
		tids.append(results['tracks']['items'][0]['uri'])

		#Find the artist in the JSON object to do an artist search
		artists = results['tracks']['items'][0]['artists']

		#Search for the artist in Spotify (using just the top artist)
		artistSearch = sp.search(q=artists[0]['name'], type='artist', limit=1)
		
		#take the genre that is associated with the artist
		genres = artistSearch['artists']['items'][0]['genres']
		
		#Get audio features using the track's ID stored in TIDS
		features = sp.audio_features(tids)
		
		#define each variable needed from the "get audio features" "search for a track" query for the project
		song_name = results['tracks']['items'][0]['name']
		popularity = results['tracks']['items'][0]['popularity']
		energy = features[0]['energy']
		dance = features[0]['danceability']
		liveness = features[0]['liveness']
		valence = features[0]['valence']
		tempo = features[0]['tempo']
		instrumental = features[0]['instrumentalness']
		acoustic = features[0]['acousticness']
		artistName = artists[0]['name']

		#store all values in a JSON
		jsonDict[index] = [song_name, artistName, energy, dance, liveness, valence, tempo, instrumental, acoustic, popularity, genres]
		print(json.dumps(features, indent=4))

#store the JSON object into a Pandas array
df = pd.DataFrame(jsonDict).T

#output these column titles in excel
df.columns = ['song', 'artist', 'energy', 'dance', 'liveness', 'valence', 'tempo', 'instrumental', 'acoustic', 'popularity', 'genres']

#output the file to excel
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

#end timer and output how long the entire search took
delta = time.time() - start
print ("features retrieved in %.2f seconds" % (delta,))