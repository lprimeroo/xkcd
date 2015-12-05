#!/usr/bin/env/python

import requests
from bs4 import BeautifulSoup
from PIL import Image
import sys
import os

def get_comic():
	r = requests.get("http://xkcd.com/")

	website_content = BeautifulSoup(r.content)

	comic_div = website_content.findAll("div", { "id" : "comic" })

	for comic in comic_div:
		comic_link =  "http:" + comic.img['src']
	return comic_link

def download_comic():
	f = open('00000000.png','wb')
	f.write( requests.get( get_comic() ).content )
	f.close()

def create_wallpaper():
	download_comic()
	comic = Image.open('00000000.png','r')
	comic_w, comic_h = comic.size

	background = Image.new('RGBA', (1440,900), (255,255,255,255))
	background_w, background_h = background.size

	offset = ( (background_w - comic_w) / 2, (background_h - comic_h) / 2 )
	background.paste(comic, offset)
	background.save('out.png')

	os.remove("00000000.png")

def os_identification():
	return sys.platform

def set_wallpaper():
	if os_identification() == "darwin":
		create_wallpaper()
		app_script = "sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db \"update data set value = '{}'\";"	.format("/Users/sarthakmunshi/Desktop/xkcd/out.png")
		os.system(app_script)
		os.system("killall Dock;")
	elif os_identification() == "linux2":
		create_wallpaper()
		linux_path = "file:///"
		mint = "gsettings set org.cinnamon.desktop.background picture-uri " + linux_path  
		ubuntu = "gsettings set org.gnome.desktop.background picture-uri " + linux_path
		try:
			os.system(mint)
		except:
			os.system(ubuntu)

if __name__ == '__main__':
	set_wallpaper()
