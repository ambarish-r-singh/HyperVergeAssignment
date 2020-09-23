import os
import sys
import time

import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print(
        "\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to "
        "take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']


def extract_text_from_image(image_file_name):
    response = ''
    retry_count = 0
    while retry_count < 3:
        try:
            ocr_url = endpoint + "vision/v3.0/ocr"
            image_path = "C:\\Users\\ambarish.singh\\PycharmProjects\\HyperVergeAssignment\\input\\images\\" + image_file_name
            image_data = open(image_path, "rb").read()
            headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
            params = {'language': 'en'}
            data = {'data': image_data}
            response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
            response.raise_for_status()
            analysis = response.json()

            line_infos = [region["lines"] for region in analysis["regions"]]
            word_infos = []
            for line in line_infos:
                for word_metadata in line:
                    for word_info in word_metadata["words"]:
                        word_infos.append(word_info["text"])
            result = "".join(word_infos)
            return result
        except:
            # print(response.headers)
            retry_duration = response.headers['Retry-After']
            time.sleep(int(retry_duration))
            retry_count = retry_count + 1
