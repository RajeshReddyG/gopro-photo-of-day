import requests
import json

url = f"https://api.unsplash.com/search/photos/?client_id=1d1792fc101c9e11d5f1b8ae165fe1c96410aaaf404a81c572e5caa2abb74a5e&query=DesktopWallpaper&per_page=1"
response = requests.get(url)

file = open("Response.json", "w+")
file.write(response.text)
file.close()

response = json.loads(response.content)
image_name = "TestImg.jpg"
image_url = "https://images.unsplash.com/photo-1556742521-9713bf272865?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjkzMDEzfQ"
image_obj = requests.get(image_url)
image_path = './images/'+image_name
with open(image_path, 'wb') as f:
    f.write(image_obj.content)
