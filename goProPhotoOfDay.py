import requests
import os
import sys
import time
qtd = int(sys.argv[1]) #Command Line Argument
url = "https://api.gopro.com/v2/channels/feed/playlists/photo-of-the-day.json?platform=web&page=1&per_page=";
url = url + str(qtd)
obj = requests.get(url);
data = obj.json();

for x in range(qtd):
	print('Getting Photo {0}...' .format(x+1))
	image_index = x;
	image_name = str(x+1)+'.jpg';
	image_url = data['media'][image_index]['thumbnails']['full']['image'];
	image_obj = requests.get(image_url);
	image_path = ''+image_name;
	with open(image_path, 'wb') as f:
			f.write(image_obj.content);
#Photoes Downloaded
#Changing Desktop Backgrounds
number = 1
while True:
    if number > qtd:
        number = 1;
    cmd="gsettings set org.gnome.desktop.background picture-uri file:///home/rajesh/Desktop/DesktopWallpaperChanger/gopro-photo-of-day/"+str(number)+".jpg"
    os.system(cmd)
    print ("wallpaper changed to %d.jpg"%number)
    number += 1
    time.sleep(4) #Change Time Accordingly
	#Hello

print('Finished script...') #Actually Never Finishes :)
