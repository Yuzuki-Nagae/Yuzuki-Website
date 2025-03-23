import streamlit as st
import pandas as pd
from streamlit_image_select import image_select

st.set_page_config(page_title = "Yuzuki's Website", layout = "wide")
st.markdown(
    """
    <style>
    body {
        background-color: #F4C2C2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.html(
    """
    <style>
    body {
        background-color: lightblues;
    }
    </style>
    """,
)
st.title("Welcome to Yuzuki's World")
st.header("My favorite anime-related videos")
images = ["/Users/Yuzuki/Desktop/documents/twiste.png"]
youtube_videos = [
    "https://www.youtube.com/embed/T8QudIpaq2Y",
    "https://www.youtube.com/embed/VhneiPkG_W0" ]
cols = st.columns(len(youtube_videos))
for i, url in enumerate(youtube_videos):
    with cols[i]:
        st.video(url)
col1, col2, = st.columns([2, 1])
with col1: 
    st.write("My favorite anime is Haikyu and Bluelock!")
    st.link_button("Read More", "https://haikyu-jp.webpkgcache.com/doc/-/s/haikyu.jp/")
with col2:
    st.image("https://eplus.jp/s/oki_img/0000168931/bluelock-exhibition/osaka/main_img.jpg", width = 300)

st.header("My favorite anime moments:)")
col3, col4, = st.columns([1, 2])
with col4: 
    st.write("「才能は開花させるもの、センスは磨くもの！」ー及川徹、「ハイキュー！！」")
    #st.button("Read More")
with col3:
    st.image("https://i.ytimg.com/vi/W6Mvefr1_iM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLColg4SCW3pfO-aMH4MzttJ34kdaw", width = 300)

col5, col6, = st.columns([2, 1])
with col5: 
    st.write("「自分を憐れむな。自分を憐れんだら人生は終わりなき悪夢だよ。」ー太宰治、「文豪ストレイドッグス」")
    #st.button("Read More")
with col6:
    st.image("https://pbs.twimg.com/media/CxlXUt_VEAIdYcM.jpg:large", width = 300)

col8, col7, = st.columns([1, 2])
with col7: 
    st.write("「８号は...僕が討伐する。」ー保科宗四郎、「怪獣８号」")
    #st.button("Read More")
with col8:
    st.image("https://times-abema.ismcdn.jp/mwimgs/c/d/375w/img_cd4bf474ea6d4f31e26104441412dd54130506.jpg", width = 300)

col9, col10, = st.columns([2, 1])
with col9: 
    st.write("「だから君に負けないように オレも頑張るよ」ー蘇枋隼飛「WIND BREAKER」")
    #st.button("Read More")
with col10:
    st.image("https://times-abema.ismcdn.jp/mwimgs/9/c/-/img_9c0212389d226f8fbd239363f1f6dd91259003.jpg", width = 300)


anime_data = [
    {
        "title": "Bungo Stray Dogs",
        "rating": 9.4,
        "genre": "Action, Fantasy",
        #"description": "The story is set in the fictional city of Yokohama. The story revolves around literary masters who use their special abilities to protect the peace of Yokohama while overcoming their own pasts.",
        "image": "https://img2.animatetimes.com/2021/11/6180ddbca303e_41ec26b387df064906c2290d27f5c12b.jpg"
    },
    {
        "title": "Haikyu!!",
        "rating": 9.6,
        "genre": "Sports",
        "description": "This is a story that depicts the growth and challenges of high school students who are passionate about volleyball.",
        "image": "https://haikyu.jp/c/themes/h/assets/img/common/visual_movie2_sp.jpg"
    },
    {
        "title": "Bluelock",
        "rating": 9.0,
        "genre": "Sports",
        "description": "Blue Lock is a story set in the Blue Lock (Blue Prison) Project, a project to train a striker who can lead Japan to victory in the World Cup.",
        "image": "https://tv.bluelock-pr.com/tv2nd/wp-content/themes/bluelock-tv2nd-theme/_assets/images/fv/fv_000_pc.png"
    },
    {
        "title": "Kaiju No.8",
        "rating": 9.2,
        "genre": "Action",
        "description": "Kaiju No. 8 is set in Japan, a monster powerhouse, and tells the story of Hibino Kafka, a cleaning worker who transforms into Kaiju No. 8 and aims to become a member of the defense force.",
        "image": "https://img2.animatetimes.com/2024/05/52c5b12402080b6230cf19c591ec3389664785a3294cf8_49765703_d8ed2c8f9e9aef86b118f42466a845d46ddee50c.jpg"
    },
]

# Convert data to a DataFrame
df = pd.DataFrame(anime_data)

# Streamlit App UI
st.title("📺 My Top Rated Anime List")
st.write("Here are some of my favorite animes with ratings and descriptions!")

# Display anime details
for index, row in df.iterrows():
    st.subheader(f"⭐ {row['title']} ({row['rating']}/10)")
    st.image(row['image'], width=200)
    st.write(f"**Genre:** {row['genre']}")
    st.write(f"📖 {row['description']}")
    st.markdown("---")
