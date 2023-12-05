import streamlit as st
from PIL import Image
import rembg
import io
import os
import time

#function to remove background
def remove_background(image_file):
    input_img = image_file.read()
    output_img = rembg.remove(input_img)
    return Image.open(io.BytesIO(output_img))

#function to merge images
def merge_images(user_image, garment_image):
    if type(garment_image) == str:
        garment_image = Image.open(garment_image)
    if type(user_image) == str:
        user_image = Image.open(user_image)
    image1_size = garment_image.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(garment_image,(0,0))
    new_image.paste(user_image,(image1_size[0],0))

    return new_image

users = {
    "Matt": "matt.webp",
    "Zlatan": "zlatan.jpeg",
    "Bob": "bob.jpeg"
}

garments = {
    "Knit Vest": "knit_vest.webp",
    "Brown Tshirt": "brown_t.webp",
    "Striped Shirt": "striped.webp",
    "Beige Sweater": "beige_sweater.webp",
    "Tight Black Sports Shirt": "tight_black.webp",
    "Resort Tshirt": "resort.webp",
}

class VtonPair():
    def __init__(self, user_name, garment_name):
        self.user_name = user_name
        self.garment_name = garment_name
    
    def get_user_image(self):
        return users[self.user_name]
    
    def get_garment_image(self):
        return garments[self.garment_name]
    
    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_garment_name(self, garment_name):
        self.garment_name = garment_name
    
    def _vton(self):
        dir = os.listdir("img/vtons/")
        files = []
        # to lowercase
        user_name = self.user_name.lower()
        garment_name = garments[self.garment_name].lower().split(".")[0]
        for file in dir:
            if user_name in file and garment_name in file:
                files.append("img/vtons/" + file)
        return files
    
    def get_merged_image(self):
        vton_images = self._vton()
        if vton_images == []:
            return [merge_images("img/user/" + self.get_user_image(), "img/garment/" + self.get_garment_image())]
        else:
            return vton_images
    
    


def main():
    st.set_page_config(layout="wide") # set layout to wide so we can use 2 columns

    st.title("Welcome to TryMeAI Virtual Try On!")
    st.markdown(
        """
        Our VITON experience helps you try on clothing from the comfort of your home, with just a few clicks! Upload your reference image of yourself, upload a garment, and see how it looks on you!
    """)

    st.header("Upload Images")
    
    col1, col2, col3, col4 = st.columns([1,1,1,1])

    simulation = VtonPair("Matt", "Knit Vest")
    with col1:
        # displaying the selected user image
        upload_user_image = st.toggle('Upload user image')
        if upload_user_image:
            user_image = st.file_uploader("Upload User Pictures", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
        else:
            selected_user_name = st.selectbox("Select User Image:", users.keys())
            simulation.set_user_name(selected_user_name)  # Update the user name in the simulation object  
            user_image = f"img/user/{simulation.get_user_image()}"  # Replace with your image paths
        st.image(user_image, width=350)

    with col2:
        upload_garment_image = st.toggle('Upload garment image')
        if upload_garment_image:
            garment_image = st.file_uploader("Upload Garment Pictures", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
        else: 
            selected_garment_name = st.selectbox("Select Garment Image:", garments.keys())
            simulation.set_garment_name(selected_garment_name)  # Update the garment name in the simulation object
            garment_image = f"img/garment/{simulation.get_garment_image()}"  # Replace with your image paths
        st.image(garment_image, width=350)


    column3_list = []
    column4_list = []


    with col3:
        if st.button("Generate"):
            if user_image and garment_image:
                # user_image = remove_background(user_image)
                with st.spinner("Generating Virtual Try On..."):
                    # sleep for 3 seconds
                    time.sleep(3)
                merged_images = simulation.get_merged_image()
                for i in range(len(merged_images)):
                    if i % 2 == 0:
                        column3_list.append(merged_images[i])
                    else:
                        column4_list.append(merged_images[i])
            else:
                st.error("Please upload both user and garment images.")
        for image in column3_list:
            st.image(image, width=350)
    with col4:
        for image in column4_list:
            st.image(image, width=350)

if __name__ == "__main__":
    main()