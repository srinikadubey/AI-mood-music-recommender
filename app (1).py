import streamlit as st
from recommender import df, recommend_by_mood
emotion_emoji = {
     "joy": "😊",
     "sadness": "😢",
     "anger": "😠",
     "fear": "😨",
     "love": "❤️",
     "surprise": "😲"
 }
 

st.title("🎵 AI Mood-Based Music Recommender")
st.write("Discover music based on how you're feeling.")

st.sidebar.title("📊 Dataset Overview")
 
st.sidebar.write(f"🎵 Total Songs: {len(df)}")
st.sidebar.write(f"👤 Artists: {df['artist'].nunique()}")
st.sidebar.write(f"🎼 Genres: {df['Genre'].nunique()}")
st.sidebar.write(f"😊 Emotion Labels: {df['emotion'].nunique()}")
mood = st.selectbox(
 " How are you feeling today?",
     ["Happy", "Sad", "Angry", "Fearful"]
 )
num_songs = st.slider("How many songs do you want?", 5, 50, 20)

if st.button("🎶 Get Recommendations"):
     results = recommend_by_mood(mood, top_n=num_songs)
 
     if results.empty:
         st.warning("No songs found for this mood.")
     else:
         st.subheader(f"Top recommendations for '{mood}'")

         for _, row in results.iterrows():
 
             st.markdown("---")
 
             col1, col2 = st.columns([3, 1])
 
             with col1:
                 st.markdown(f"### 🎵 {row['song']}")
                 st.write(f"👤 **Artist:** {row['artist']}")
                 st.write(f"🎼 **Genre:** {row['Genre']}")
                 emo = row["emotion"]
                 emoji = emotion_emoji.get(emo, "🎵")
 
                 st.write(f"{emoji} {emo}")
             with col2:
                 st.metric("🔥 Popularity", row["Popularity"])
                 st.metric("⚡ Energy", row["Energy"])
                 st.metric("💃 Danceability", row["Danceability"])

    
