import streamlit as st
import skimage


# Function definitions

def get_image(image_file):
    # Convert image into an ndarray
    img = skimage.io.imread(image_file)
    # TODO: Image preprocessing?
    return img

def load_model():
    # TODO: Load model
    model = None
    return model

def process_image(model, img):
    # TODO: Apply model on provided image
    result = img
    return result


# Image upload form

st.title('Peripheral Blood Smear Differential')
st.write('Upload a peripheral blood smear image')

image_file = st.file_uploader('Upload Image', type=['jpg', 'png'])


# Result image

if image_file is not None:
    img = get_image(image_file)
    model = load_model()
    result_image = process_image(model, img)
    
    st.header('Result')
    st.image(result_image)
