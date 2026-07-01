import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('/content/data/light_spotify_dataset.csv')
df = df.dropna(subset=["song", "artist"])


df = df[df["emotion"] != "True"]

df = df.sample(20000, random_state=42).reset_index(drop=True)


features = ['variance','Tempo','Loudness','Popularity','Energy',
'Danceability','Positiveness','Speechiness','Liveness',
'Acousticness','Instrumentalness']

df_features = df[features].fillna(0)

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df_features)
mood_map = {
     "Happy": ["joy", "love", "surprise"],
     "Sad": ["sadness"],
     "Angry": ["anger"],
     "Fearful": ["fear"]
 }
def get_mood_df(mood):
     if mood not in mood_map:
         return df
 
     return df[df["emotion"].isin(mood_map[mood])]
def recommend_by_mood(mood, top_n=10):
 
     mood_df = get_mood_df(mood).copy()
 
     if len(mood_df) == 0:
         return pd.DataFrame()
 
     mood_features = scaler.transform(mood_df[features]) 

     mood_vector = np.mean(mood_features, axis=0).reshape(1, -1)
     similarity = cosine_similarity(mood_vector, mood_features).flatten()
 
     top_indices = similarity.argsort()[::-1][:top_n]
     return mood_df.iloc[top_indices][[
         "song",
         "artist",
         "Genre",
         "emotion",
         "Popularity",
         "Energy",
         "Danceability"
     ]]
