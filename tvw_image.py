"""
Import images with APIs 
- write a function for the retrieving of the images, with arguments that are then the specific for each image?
- upload images in the cloud in order to have an url
- do I need an API key? And how to get it 
"""
# from lesson:

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import requests


# Astronomy Picture of the Day:
API_KEY = 'ZaIvDcu36AW45sXrdEsgSNwBaNhmIfWO1IrkJbdW'
response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")


# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    image_url = data['url']
    title = data['title']
    explanation = data['explanation']

    # Fetch the image
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))

    # Display the image using matplotlib
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.title(title)
    plt.show()

    # Print the explanation
    print(f"Title: {title}\n")
    print(f"Explanation: {explanation}")
else:
    print(f"Failed to retrieve data: {response.status_code}")