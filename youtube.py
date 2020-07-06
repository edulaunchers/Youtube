import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import csv
import pandas as pd
titl = []
description = []
views = []
date_published = []
likes = []
dislikes = []
channel_tag = []
subscribers = []
def youtube():
	quote = {} 
	quotes=[]
	video_url = "https://www.youtube.com/watch?v=QcDqtbtw-zI"
	content = requests.get(video_url)
	soup = bs(content.content, "html.parser")
	print(soup)
	
	titl.append(soup.find("span", attrs={"class": "title"}).text)
	print(titl)
	
	try:
		description.append(soup.find("p", attrs={"id": "eow-description"}).text)
	except:
		pass
	try:
		views.append(int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", "")))
	except:
		pass
	try:
		date_published.append( soup.find("strong", attrs={"class": "watch-time-text"}).text)
	except:
		pass
	try:
		likes.append(str(int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))))
	except:
		pass
	try:
		dislikes.append(str(int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))))
	except:
		pass
	try:
		channel_tag.append( soup.find("a", attrs={"class": "yt-uix-sessionlink spf-link"}).text)
	except:
		pass
	try:
		subscribers.append(soup.find("span", attrs={"class": "yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count"}).text)
	except:
		pass
	df_marks=pd.DataFrame({'Title':titl,'Description':description,'Views':views,'Date_published':date_published,'Likes':likes,'Dislikes':dislikes,'Channel Name':channel_tag,'Subscribers':subscribers})
	df_marks.to_csv('youtube.csv', mode='a')
	
if __name__ == '__main__':
	youtube()