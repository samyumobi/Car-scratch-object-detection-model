import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
def import_and_predict(image_data, model):
    
        size = (150,150) 
        image = ImageOps.fit(image_data)
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)

        img_reshape = image[np.newaxis,...]

    
        prediction = model.predict(img_reshape)
        
        return prediction
    
model = tf.keras.models.load_model('car_model.hdf5')

import streamlit as st
st.write("""
         # Car Damage Detection
         """
         )
st.write("This is a simple image classification web app to predict damage")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])    
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) < 0.5:
        st.write("Car Damage!")
    elif np.argmax(prediction) >= 0.5:
        st.write("Car Not Damage!")
    
    
    st.text("Probability (0: Car_Damage, 1: Car_Not_Damage")
    st.write(prediction)
