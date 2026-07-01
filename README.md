
## 🎵 AI Mood-Based Music Recommender

An interactive music recommendation web application built using Machine Learning and Streamlit. The application recommends songs based on the user's selected mood by analyzing audio features such as Energy, Danceability, Tempo, Loudness, Popularity, Acousticness, and more.

Instead of requiring users to search for a song, the application generates recommendations directly from the selected mood, making music discovery simple and intuitive.

### Live Demo

* Streamlit App: (Add your deployed Streamlit link here after deployment.)

### Features

* 😊 Mood-based song recommendations
* 🤖 Machine Learning using cosine similarity
* 📊 Audio feature normalization using MinMaxScaler
* 🎼 Displays song, artist, genre, emotion, popularity, energy, and danceability
* ▶️ One-click YouTube search for each recommended song
* 🌐 Interactive web application built with Streamlit

### Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

### Dataset

Spotify Songs Dataset containing:

* Song Name
* Artist
* Genre
* Emotion
* Popularity
* Energy
* Danceability
* Tempo
* Loudness
* Acousticness
* Instrumentalness
* Speechiness
* Liveness

### Machine Learning Workflow

1. Load and clean the dataset.
2. Select relevant audio features.
3. Normalize features using MinMaxScaler.
4. Filter songs based on the selected mood.
5. Compute cosine similarity to identify songs with similar audio characteristics.
6. Display the top recommendations through an interactive Streamlit interface.

### Future Improvements

* Spotify API integration
* Album artwork
* Audio previews
* Personalized recommendations based on listening history
* Collaborative filtering
