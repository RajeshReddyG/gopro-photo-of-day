import requests
import os
import sys
import time
import json

qtd = int(sys.argv[1])  # Command Line Argument
headers = {
    "Authorization": "563492ad6f91700001000001f11d9b566e5145e5895dafde5a2c3c34",
}

url = f"https://api.pexels.com/v1/search?query=Desktop Wallpaper&per_page=1&page=1"
# url = f"https://api.pexels.com/v1/curated?per_page=1&page=1"

response = requests.get(url, headers=headers)

file = open("Response.json", "w+")
file.write(response.text)
file.close()

response = json.loads(response.content)
if(response["total_results"] != 0):
    NameStr = response["photos"][0]["url"]
    image_name = NameStr[29:-9]+".jpg"
    image_url = response["photos"][0]["src"]["original"]
    image_obj = requests.get(image_url)
    # image_path = 'C:\\Users\\Rajesh.Gundupalli\\Desktop\\GitHub\\gopro-photo-of-day\\images\\'+image_name
    image_path = './images/'+image_name
    with open(image_path, 'wb') as f:
        f.write(image_obj.content)
else:
    print("No Results... :(")
# Photoes Downloaded

# Changing Desktop Backgrounds
number = 1
while True:
    if number > qtd:
        number = 1
	#ToDo: Work on Path and Name
    cmd = "gsettings set org.gnome.desktop.background picture-uri file:///home/rajesh/Desktop/DesktopWallpaperChanger/gopro-photo-of-day/" + \
        str(number)+".jpg"
    os.system(cmd)
    print("wallpaper changed to %d.jpg" % number)
    number += 1
    time.sleep(4)  # Change Time Accordingly
    # Hello

print('Finished script...')  # Actually Never Finishes :)
