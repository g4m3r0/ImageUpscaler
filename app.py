from flask.wrappers import Response
from flask import Flask, request, render_template
import cv2
import os
import time
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"
app = Flask(__name__)

# Load SRCNN model
SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"
model = None

# Define function for image upscaling and enhancement
def enhance_image(img):
    pp_image = preprocess_image(img)

    start = time.time()
    upscaled_img = model(pp_image)
    upscaled_img = tf.squeeze(upscaled_img)
    print("Time Taken: %f" % (time.time() - start))
    
    # https://www.javatpoint.com/fastnlmeansdenoising-in-python
    # enhanced_img = cv2.fastNlMeansDenoisingColored(upscaled_img, None, 10, 10, 7, 21)
    return upscaled_img

def preprocess_image(pp_image):
  """ Loads image from path and preprocesses to make it model ready
      Args:
        pp_image: image file
  """
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
  if pp_image.shape[-1] == 4:
    pp_image = pp_image[...,:-1]
  hr_size = (tf.convert_to_tensor(pp_image.shape[:-1]) // 4) * 4
  pp_image = tf.image.crop_to_bounding_box(pp_image, 0, 0, hr_size[0], hr_size[1])
  pp_image = tf.cast(pp_image, tf.float32)
  return tf.expand_dims(pp_image, 0)


# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route for image upload
@app.route('/upload', methods=['POST'])
def upload():
    # Load uploaded image
    file = request.files['image']

    # Read bytes and convert them to image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Enhance image
    enhanced_img = enhance_image(img)

    print(f"Original Shape: {img.shape}")
    print(f"Enhanced Shape: {enhanced_img.shape}")

    # Encode enhanced image
    numpy_image = enhanced_img.numpy()
    _, encoded_img = cv2.imencode('.jpg', numpy_image)
    byte_image = encoded_img.tobytes()

    # Encode original image
    _, encoded_orig_img = cv2.imencode('.jpg', img)
    encoded_orig_img = encoded_orig_img.tobytes()

    # Create response
    #response = []
    #response.append(Response(byte_image, mimetype='image/jpeg'))
    #response.append(Response(encoded_orig_img, mimetype='image/jpeg'))
    response = Response(byte_image, mimetype='image/jpeg')

    return response

if __name__ == '__main__':
    # Initialize model
    model = hub.load(SAVED_MODEL_PATH)
    app.run(debug=True)