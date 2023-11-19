import streamlit as st
from PIL import Image
import rembg
import io

def remove_background(image_file):
    input_img = image_file.read()
    output_img = rembg.remove(input_img)
    return Image.open(io.BytesIO(output_img))

def main():
    st.title("Welcome to TryMeAI Virtual Try On!")
    st.markdown(
        """
        Our VITON experience helps you try on clothing from the comfort of your home, with just a few clicks! Upload your reference image of yourself, upload a garment and see how it looks on you!
    """
    )

    st.sidebar.header("Upload Images")
    uploaded_user_image = st.sidebar.file_uploader("Upload User Picture", type=["png", "jpg", "jpeg"])
    uploaded_garment_image = st.sidebar.file_uploader("Upload Garment Picture", type=["png", "jpg", "jpeg"])

    if uploaded_user_image and uploaded_garment_image:
        st.header("User Picture")
        with st.spinner('Processing User Image...'):
            processed_user_image = remove_background(uploaded_user_image)
            st.image(processed_user_image, caption='User Picture (Background Removed)', use_column_width=True)

        st.header("Garment Picture")
        with st.spinner('Processing Garment Image...'):
            processed_garment_image = remove_background(uploaded_garment_image)
            st.image(processed_garment_image, caption='Garment Picture (Background Removed)', use_column_width=True)

        
        resized_user_image = processed_user_image.resize((200, 200))  # Adjust size as needed
        resized_garment_image = processed_garment_image.resize((200, 200))  # Adjust size as needed

        
        st.header("VITON experience!")
        col1, col2 = st.columns(2)
        with col1:
            st.image(resized_user_image, caption='User Image', use_column_width=False)
        with col2:
            st.image(resized_garment_image, caption='Garment Image', use_column_width=False)

if __name__ == "__main__":
    main()

