# Mental Health as a Function of Music - Data Mining 

An exploratory research to find any correlation between a listener's preference in music and their mental health.

Python and Spotipy (Python Spotify Web Wrapper) were used to create the data mining models and to retrieve song information from Spotify's Web API.

Table of Contents
-----------------

   * [Mental Health as a Function of Music - Data Mining](#mental-health-as-a-function-of-music---data-mining)
      * [Data Collection](#data-collection)
      * [Exploratory Data Analysis](#exploratory-data-analysis)
         * [Univariate Data](#univariate-data)
            * [General Graphs](#general-graphs)
            * [Music Graphs](#music-graphs)
            * [Mental Health Graph](#mental-health-graph)
         * [Bivariate Data](#bivariate-data)
            * [Scatter Plots](#scatter-plots)
      * [Feature Engineering](#feature-engineering)
         * [Recursive Feature Elimination (RFE)](#recursive-feature-elimination-rfe)
      * [Regression](#regression)
         * [Linear Regression](#linear-regression)
         * [Multiple Linear Regression](#multiple-linear-regression)
      * [Association](#association)



## Data Collection

The primary data was collected through a survey that asked surveyers to list their 3 favourite songs at the moment and to rate their mental health using a likert scale. The following questions were asked as they are described to be good indicators of an individual's mental health by the [Canadian Mental Health Association](www.cmha.ca/mental_health/mental-health-meter/):

- ability to enjoy life
- resilience
- balanced lifestyle
- emotional flexibility
- self-actualization

The survey also collected general data such as:

- gender
- age range
- hours of music they listen to per day
- if they have experienced anything unusual/traumatic recently (to help ensure music is the main factor contributing to mental health)

Once the survey had more than 300 entries (and approximately 1000 songs), a Python script was made to fetch data from Spotify's music catalog using Spotify Web API. The  [Get Audio Features for a Track](https://developer.spotify.com/web-api/get-audio-features/) endpoint was used to retrieve song information in a JSON format. An example of this JSON output is shown below for a song.

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

#### General Graphs
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

Tempo, popularity, energy, dance and valence have a nice normal distribution which shows that listeners listen to a variety of music hovering around a mean of <b> 123 bpm, 61 popularity, 0.65 energy, 0.60 danceability, 0.45 valence</b>. The entire dataset is primarily not listening to instrumental tracks as shown by the instrumentalness graph which means we can drop this feature as it is least likely to be contributing to mental health. However let's keep exploring the data set before removing any features.

#### Mental Health Graph
![Figure12](https://github.com/sunnyshikhar/music-datamining/blob/master/images/mentalHealthHisto.png?raw=true) 
The mental health histogram is also normally distributed around a mental health
score between 21-23. There are significantly less people with a low mental health
score as majority of the people have a medium to high mental health score.

### Bivariate Data

#### Scatter Plots
The following graphs plot mental health as a function of each musical feature.
![Figure14](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsTempo.png?raw=true)
![Figure14](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsPopularity.png?raw=true)
![Figure15](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsEnergy.png?raw=true)
![Figure16](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsDanceability.png?raw=true) 
![Figure17](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsValence.png?raw=true) 
![Figure18](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsLiveness.png?raw=true)
![Figure19](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsAcousticness.png?raw=true)
![Figure20](https://github.com/sunnyshikhar/music-datamining/blob/master/images/healthVsInstrumentalness.png?raw=true) 

The scatter plot does not show any clear relationship between mental health and any musical feature (such as linear, logarithmic etc). However, we are able to conclude that instrumentalness is a weak feature in potentially predicting mental health as mental health ranges from 5 to 30 for really low instrumental values. To say this conclusively, let's do some feature engineering to ensure the right attributes are being used to predict mental health.

## Feature Engineering

### Recursive Feature Elimination (RFE)

The Recursive Feature Elimination (RFE) method is a feature selection approach. It works by recursively removing attributes and building a model on those attributes that remain. It uses the model accuracy to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute. Using sklearn's LogisticRegression and RFE library, the following features were found to have the most impact on the mental health class variable. 

| Rank  | Song Attribute  |
|:-:|---|
|  1 | Energy  |
|  2 | Danceability |
|  3 | Popularity  |
|  4 | Tempo  |
|  5 | Valence  |
|  6 | Acousticness  |
|  7 | Liveness  |
|  8 | Instrumentalness  |

As expected, instrumentalness is the least important feature along with livness and acousticness. Therefore, these three features were removed for the remainder of the study in building more models.

## Regression

### Linear Regression

As noticed through scatter plots, there is no graph that distinctly shows any linear or non-linear relationship. Therefore, more scatter plots were investigated. When plotting danceability of songs for people who said they went through a traumatic experience and those who didn't with mental health hinted that there might be a relationship present. Although the scatter plot is still difficult to interpret, the filtered plot is shown below:

![Figure](https://github.com/sunnyshikhar/music-datamining/blob/master/images/traumaScatter.png?raw=true) 

Based on the observations of the scatter plots, it was hypothesized that linear regression model would not be the best model to represent the dataset.To conclude this hypothesis, a linear regression analysis was conducted on mental health score relative to the danceability factor for individuals who recently encountered a traumatic experience. Danceability song attribute was chosen as the scatter plot resembled the most to a
linear trend in comparison to other song attributes. 

![Figure](https://github.com/sunnyshikhar/music-datamining/blob/master/images/traumaRegression.png?raw=true)
![Figure](https://github.com/sunnyshikhar/music-datamining/blob/master/images/traumaResidualHisto.png?raw=true)
![Figure](https://github.com/sunnyshikhar/music-datamining/blob/master/images/residualDistribution.png?raw=true)

| Field  | Value  |
|:-:|---|
| Coefficients (m))  | 15.21 |
| Intercept (b) | 8.94 |
| Equation of the Line  | Mental Health = (15.21)(danceability) + 8.94 |
| Mean Residual Sum of Squares  | 19.59  |
| RMSE  |  4.42  |
| R-Squared  | 0.14  |
| Mean of Residuals  | 4.42   |
| Standard Deviation of Results |  4.42  |


The residual plot of mental health scores against danceability showed a normal distribution concentrated around zero. This validates that a linear regression model is an appropriate model although not an applicable one due to such a wide spread of data points. The R-squared value obtained for the linear regression model was 14% which is fairly low. This further shows that the model does not account for much variability in
the data.

### Multiple Linear Regression

In order to improve the r-squared value, a multiple regression was conducted using the top 5 features from RFE to predict Mental Health. Sklearn's linear_model library was used which uses the Ordinary Least Squares (OLS) method to conduct it's multiple linear regression. OLS or linear least squares method computes the least squares solution using a singular value decomposition of X. This means the algorithm attempts to minimize the sum of squares of residuals. The output is shown below. 

![Figure](https://github.com/sunnyshikhar/music-datamining/blob/master/images/OLSregression.png?raw=true)

The R-squared value increases from 13% in the linear regression to 20.5% in the multi linear regression. However, it is still a weak r-squared value. However, the adjusted r-squared is significantly lower at 15.8%. The adjusted R-squared is a modified version of R-squared that has been adjusted for the number of predictors in the model. This could mean that even 5 features are too many (or too few) to predict mental health and that the gap between r-squared and adjusted r-squared could be less by adding or removing features. 

Regardless, it is conclusive that a linear model is not an accurate model to represent mental health and musical features. Let's keep searching!

## Association 

The purpose of association was to find patterns in the data along with analyzing the relationships between various attributes. Based on the scatter plots analyzed previously, it was hypothesized that with a high confidence level, the categorical variable mental health will not be part of any rules. This is because mental health did not consistently correlate with any of the song attributes. In addition, 87.5% of the dataset consisted of people from ages 18-20 years old. It is assumed that the age range categorical variable will be associated with a lot of attributes due to it abundance of 18-20 year olds in the dataset.

The APRIORI algorithm was used for association rule mining. Since there were only 255 unique records, a minimum support of ten percent was chosen so each rule would cover at least 25 records. If there was a much larger dataset, a lower support percentage would have been chosen. For example, for a million records, a support of one percent would be chosen as it covers 10,000 records. A support of 10-20 percent is a reasonable assumption for the current dataset. 

As expected, association rules for mental health had a very low confidence. There are several reasons as to why the APRIORI algorithm did not generate good association rules for mental health based on the dataset. One factor could be that music may not be a dominant influence on a person’s mental health leading to poor association rules. Another factor could be the lack of song data. However, a few interesting associations are shown below: 

High Popularity + High Valence -----> High Danceability (96.7% Confidence)

Low Popularity + Low Valence   -----> Low Danceability (94.1% Confidence)
 