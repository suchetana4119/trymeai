import streamlit as st
from PIL import Image, ImageDraw
import rembg
import io

#function to remove background
def remove_background(image_file):
    input_img = image_file.read()
    output_img = rembg.remove(input_img)
    return Image.open(io.BytesIO(output_img))

#function to merge images
def merge_images(user_image, garment_image):
    garment_resized = garment_image.resize(user_image.size)
    merged_image = Image.new('RGBA', user_image.size)
    merged_image.paste(user_image, (0, 0))
    merged_image.paste(garment_resized, (0, 0), garment_resized)
    return merged_image

def main():
    st.title("Welcome to TryMeAI Virtual Try On!")
    st.markdown(
        """
        Our VITON experience helps you try on clothing from the comfort of your home, with just a few clicks! Upload your reference image of yourself, upload a garment, and see how it looks on you!
    """)

    st.header("Upload Images")

    #predefined images
    predefined_user_images = [
        "Select User Image",
        "User Image 1",
        "User Image 2",
        "User Image 3",
        "User Image 4"
    ]

    predefined_garment_images = [
        "Select Garment Image",
        "Garment Image 1",
        "Garment Image 2",
        "Garment Image 3",
        "Garment Image 4"
    ]

    
    col1, col2 = st.columns(2)

    with col1:
        selected_user_image = st.selectbox("Select User Image:", predefined_user_images)

        #displaying the selected user image
        if selected_user_image != "Select User Image":
            user_image_path = f"path_to_your_preuploaded_images/{selected_user_image}.png"  # Replace with your image paths
            user_image = Image.open(user_image_path)
            st.image(user_image, caption='Selected User Image', use_column_width=True)

    with col2:
        selected_garment_image = st.selectbox("Select Garment Image:", predefined_garment_images)

        #displaying the selected garment image
        if selected_garment_image != "Select Garment Image":
            garment_image_path = f"{selected_garment_image}.png"  # Replace with your image paths
            garment_image = Image.open(garment_image_path)
            st.image(garment_image, caption='Selected Garment Image', use_column_width=True)

    #upload area for user image and garment image
    uploaded_user_images = st.file_uploader("Upload User Pictures", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    uploaded_garment_images = st.file_uploader("Upload Garment Pictures", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if uploaded_user_images and uploaded_garment_images:
        pass 

if __name__ == "__main__":
    main()