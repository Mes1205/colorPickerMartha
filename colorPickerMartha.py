import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Color Picker", layout="centered")

st.title("🎨 Color Picker dari Gambar")
st.write("Upload foto yang mau diliat 5 warna dominannya sebagai palet warna.")

uploaded_file = st.file_uploader("Upload di sini yeaaa", type=["jpg", "jpeg", "png"])

def get_dominant_colors(image, num_colors=5):
    img = image.resize((150, 150))  # resize untuk mempercepat proses
    img_np = np.array(img)
    img_np = img_np.reshape((-1, 3))  # ubah ke array 2D
    kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(img_np)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Gambar yang Diunggah", use_column_width=True)

    colors = get_dominant_colors(image)

    st.subheader("Palet Warna Dominan:")
    cols = st.columns(len(colors))
    for idx, col in enumerate(cols):
        rgb = tuple(colors[idx])
        hex_color = '#%02x%02x%02x' % rgb
        col.markdown(
            f"<div style='background-color:{hex_color}; width:100px; height:100px;'></div>"
            f"<p style='text-align:center'>{hex_color}</p>",
            unsafe_allow_html=True
        )