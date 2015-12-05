import requests
from bs4 import BeautifulSoup
from PIL import Image

def get_comic():
	r = requests.get("http://xkcd.com/")

	website_content = BeautifulSoup(r.content)

	comic_div = website_content.findAll("div", { "id" : "comic" })

	for comic in comic_div:
		comic_link =  "http:" + comic.img['src']
	return comic_link

def download_comic():
	f = open('00000001.png','wb')
	f.write( requests.get( get_comic() ).content )
	f.close()

def create_wallpaper():
	comic = Image.open('00000001.png','r')
	comic_w, comic_h = comic.size
	background = Image.new('RGBA', (1440,900), (255,255,255,255))
	background_w, background_h = background.size
	offset = ( (background_w - comic_w) / 2, (background_h - comic_h) / 2 )
	background.paste(comic, offset)
	background.save('out.png')


download_comic()
create_wallpaper()
