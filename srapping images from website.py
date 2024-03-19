import requests
from bs4 import BeautifulSoup
import os

url = "https://www.udemy.com/?utm=1c5408ecf63ccf3d0d9bd4803d9d8838&track=1&pt=2"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
image_elements = soup.find_all('img')

output_directory = 'downloaded_images'
os.makedirs(output_directory, exist_ok=True)

for index, img in enumerate(image_elements):
    source = img.get('src')
    
    # Check if the 'src' attribute exists and if it starts with 'http' (indicating an image)
    if source and source.startswith('http'):
        image_response = requests.get(source)
        if image_response.status_code == 200:
            image_data = image_response.content
            image_extension = source.split('.')[-1]
            image_filename = f'image_{index}.{image_extension}'
            image_path = os.path.join(output_directory, image_filename)

            with open(image_path, 'wb') as f:
                f.write(image_data)
                
            print(f"Downloaded: {image_filename}")
        else:
            print(f"Failed to download image {index}")
    else:
        print(f"Skipped non-image element {index}")

    
     

