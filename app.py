import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import cv2
import numpy as np
from pyngrok import ngrok
from keras.preprocessing.image import img_to_array


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('/content/my_model2.hdf5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Flower Classification
         """
         )

file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np
st.set_option('deprecation.showfileUploaderEncoding', False)
def import_and_predict(image_data, model):

        size = (180,180)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),interpolation=cv2.INTER_CUBIC))/255.
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction
  
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    st.write(prediction)
    st.write(score)
    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

# Mengonfigurasi pyngrok untuk membuat tunnel
public_url = ngrok.connect(port='8501')

# Menampilkan URL ngrok
st.write('**Ngrok Tunnel URL:**', public_url)
