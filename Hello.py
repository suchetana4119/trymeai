import streamlit as st
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="VITON")

st.write("# Welcome to TryMeAI Virtual Try On!")
st.sidebar.write("## Upload your image :gear:")
st.markdown(
        """
        Our VITON experience helps you try on clothing from the comfort of your home, with just a few clicks! Upload your reference image of yourself, upload a garment and see how it looks on you!
    """
    )
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

st.sidebar.write("## Upload your garment :gear:")

col3, col4 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"],key = "<uniquevalueofsomesort>")