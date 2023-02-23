import streamlit as st
import requests

# Generate a key from NASA
api_key = "EtlasAUeL8hLYkdBwHycq7SWaU1bcQqGaaWBykrb"
url = "https://api.nasa.gov/planetary/apod?api_key=EtlasAUeL8hLYkdBwHycq7SWaU1bcQqGaaWBykrb"

r = requests.get(url)

content = r.json()

print(content)

title = content['title']
des = content['explanation']

image = content['hdurl']
response = requests.get(image)
with open("image.jpg", 'wb') as file:
    file.write(response.content)

st.title(title)
st.image(image)
st.write(des)
