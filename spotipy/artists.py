from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

if len(sys.argv) > 1:
    track_name = ''.join(sys.argv[1:])
    results = sp.search(q=track_name, limit=1)
    tids = []
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'], t['artists'])
        tids.append(t['uri'])

    start = time.time()
    features = sp.audio_features(tids)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print ("features retrieved in %.2f seconds" % (delta,)) 