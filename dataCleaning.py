import pandas as pd

# Survey Data Cleaning
survey = pd.read_csv('data/survey.csv')
survey['id'] = survey.index
survey.columns = ['timestamp', 'gender', 'age', 'amount_music', 'life_enjoyment', 'resilience', 
                  'balanced_life', 'emotional_flex', 'self_actualization', 'song1', 'song2', 'song3', 'trauma', 'id']
survey['total_health'] = (survey['life_enjoyment'] + survey['resilience'] + survey['balanced_life'] + 
                          survey['emotional_flex'] + survey['self_actualization'])

## Clean song strings for sending to Spotify API
survey['song1'] = survey['song1'].str.replace('by', '').str.replace('-', '').str.replace(',','').str.replace('  ', ' ')
survey['song2'] = survey['song2'].str.replace('by', '').str.replace('-', '').str.replace(',','').str.replace('  ', ' ')
survey['song3'] = survey['song3'].str.replace('by', '').str.replace('-', '').str.replace(',','').str.replace('  ', ' ')

## Arrange songs by ID for Spotify API
songs_only = pd.DataFrame(columns=['id','songs'])

for index, row in survey.iterrows():
    songs_only = songs_only.append({'id' : row['id'] , 'songs' : row['song1']}, ignore_index=True)
    songs_only = songs_only.append({'id' : row['id'] , 'songs' : row['song2']}, ignore_index=True)
    songs_only = songs_only.append({'id' : row['id'] , 'songs' : row['song3']}, ignore_index=True)
    
songs_only.to_csv('data/songs_only.csv', index=False)

# Retrieve audio features using spotipy.py

# Cleaning audio features from Spotify API output
song_metrics = pd.read_csv('data/song_metrics.csv')

avg_metrics = song_metrics.groupby('id').mean()

master = pd.merge(survey, avg_metrics, on='id')
master = master.drop(columns=['Unnamed: 0'])

## Creating categorical variable for mental health
master.loc[master['total_health'] > 15, 'health_categorical'] = 1
master.loc[master['total_health'] <= 15, 'health_categorical'] = 0

master.to_csv('data/master.csv', index=False)