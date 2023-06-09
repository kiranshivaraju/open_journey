import base64
import requests
from io import BytesIO
from PIL import Image

model_inputs = {
    'f1 car in the evening on a track',
}

res = requests.post('http://localhost:8000/', json = model_inputs)

image_byte_string = res.json()["image_base64"]
image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")