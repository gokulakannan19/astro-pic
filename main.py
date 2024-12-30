import os
import requests
import streamlit as st

DEMO_KEY = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={DEMO_KEY}"
request = requests.get(url)
content = request.json()

st.header(content["date"])
st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
