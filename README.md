# Mental Health as a Function of Music - Data Mining 

An exploratory research to find any correlation between a listener's preference in music and their mental health.

Python and Spotipy (Python Spotify Web Wrapper) were used to create the data mining models and to retrieve song information from Spotify's Web API.

## Data Collection

The primary data was collected through a survey that asked surveyers to list their 3 favourite songs at the moment and to rate their mental health using a likert scale on the following topics:

- ability to enjoy life
- resilience
- balanced lifestyle
- emotional flexibility
- self-actualization

These questions are described as good indicators of an individual's mental health by the [Canadian Mental Health Association](www.cmha.ca/mental_health/mental-health-meter/).

Once the survey had more than 300 entries (and approximately 1000 songs), a Python script was made to fetch data from the Spotify's music catalog using Spotify Web API. The  [Get Audio Features for a Track](https://developer.spotify.com/web-api/get-audio-features/) endpoint was used to retrieve song information in a JSON format. An example of this JSON output is shown below for a song.

<b>"Starboy - The Weeknd ft. Daft Punk"</b>

[{
- "track_href": "https://api.spotify.com/v1/tracks/7MXVkk9YMctZqd1Srtv4MB",
- "type": "audio_features",
- "analysis_url": "https://api.spotify.com/v1/audio-analysis/7MXVkk9YMctZqd1Srtv4MB",
- "acousticness": 0.168,
- "speechiness": 0.284,
- "liveness": 0.136,
- "uri": "spotify:track:7MXVkk9YMctZqd1Srtv4MB",
- "id": "7MXVkk9YMctZqd1Srtv4MB",
- "key": 7,
- "mode": 1,
- "time_signature": 4,
- "duration_ms": 230453,
- "tempo": 185.998,
- "danceability": 0.675,
- "valence": 0.49,
- "instrumentalness": 3.36e-06
}]

For the purposes of this study, only the following features were retrieved: 

| Feature  | Definition by Spotify  |
|:-:|---|
| Energy |Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. |
| Danceability | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.  |
| Valence  |  A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).  |
| Tempo  | The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. |
| Popularity  | The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.  |
| Instrumentalness  | 	Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.  |
|  Acousticness | 	A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.  |
| Liveness  | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. |

Once the data was collected, it was cleaned to ensure that there were no missing fields. Furthermore, each listener's total mental health score was calculated as a sum of the individual mental health answers and an average of their musical properties were taken to reflect the listener's overall musical behaviour. 

Now that all the data has been collected and cleaned, time to get into the more interesting material!

## Exploratory Data Analysis

Let's begin by plotting bar charts and histograms of each variable obtained from the survey and spotify to understand it's distribution, mode, variance etc. 

### Univariate Data

#### Surveyers Graph
![Figure1](https://github.com/SunnyShikhar/music-datamining/blob/master/images/genderHistogram.png?raw=true) 
![Figure2](https://github.com/sunnyshikhar/music-datamining/blob/master/images/hoursDurationHisto.png?raw=true) 
![Figure3](https://github.com/sunnyshikhar/music-datamining/blob/master/images/ageHistogram.png?raw=true) 

53.8% of the data set consists of females, 45.3% males and less than 1% chose not to specify.

Surprisingly, <b>46.6%</b> of the data set listens to 2+ hours of music, <b>35%</b> listen to 1-2 hours and <b>18.4%</b> listen to 0 - 1 hours of music. It was expected that most people would be listening to 1-2 hours, but we underestimated the number of avid music listeners. 

Similarly, our data set primariy consisted of 18-30 year olds. We realzied later that this was too large of a range and should have been divided further.

#### Music Graphs
![Figure4](https://github.com/sunnyshikhar/music-datamining/blob/master/images/tempoHistogram.png?raw=true) 
![Figure5](https://github.com/sunnyshikhar/music-datamining/blob/master/images/popularityHistogram.png?raw=true) 
![Figure6](https://github.com/sunnyshikhar/music-datamining/blob/master/images/energyHistogram.png?raw=true) 
![Figure7](https://github.com/sunnyshikhar/music-datamining/blob/master/images/danceHistogram.png?raw=true) 
![Figure8](https://github.com/sunnyshikhar/music-datamining/blob/master/images/valenceHistogram.png?raw=true) 
![Figure9](https://github.com/sunnyshikhar/music-datamining/blob/master/images/livenessHistogram.png?raw=true) 
![Figure10](https://github.com/SunnyShikhar/music-datamining/blob/master/images/acousticHistogram.png?raw=true) 
![Figure11](https://github.com/sunnyshikhar/music-datamining/blob/master/images/instrumentalnessHistogram.png?raw=true) 
Tempo, popularity, energy, dance and valence have a nice normal distribution which shows that listeners listen to a variety of music hovering around a mean of <b> 123 bpm, 61 popularity, 0.65 energy, 0.60 danceability, 0.45 valence</b>. Our entire dataset is primarily not listening to instrumental tracks as shown by the instrumentalness graph which means we can drop this feature as it least likely to be contributing to mental health. However let's keep exploring the data set before removing any features.

#### Mental Health Graph
![Figure12](https://github.com/sunnyshikhar/music-datamining/blob/master/images/mentalHealthHisto.png?raw=true) 
The mental health histogram is also normally distributed around a mental health
score between 21-23. There are significantly less people with a low mental health
score as majority of the people have a medium to high mental health score.

### Bivariate Data

#### Scatter Plots
The following graphs plot mental health as a function of each musical feature.
![Figure13](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsTempo.png?raw=true)
![Figure14](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsPopularity.png?raw=true)
![Figure15](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsEnergy.png?raw=true)
![Figure16](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsDanceability.png?raw=true) 
![Figure17](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsValence.png?raw=true) 
![Figure18](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsLiveness.png?raw=true)
![Figure19](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsAcousticness.png?raw=true)
![Figure20](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsInstrumentalness.png?raw=true) 

The scatter plot does not show any clear relationship between mental health and any musical feature (such as linear, logarithmic etc). However, we are able to conclude that instrumentalness is a weak feature in potentially predicting mental health as mental health ranges from 5 to 30 for really low instrumental values. To say this conclusively, let's do some feature engineering to ensure the right attributes are being used to predict mental health.