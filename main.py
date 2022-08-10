import colored
from colored import stylize
import requests
from RedDownloader import RedDownloader
from random import randint
import multiprocessing
import moviepy
import moviepy.editor as mp
from moviepy.editor import *
from time import sleep
from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime
print(stylize("RedditMemesMaker",colored.fg("green")))

'''
def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest

keyauthapp = api(
	name = "MemesVideoMaker",
	ownerid = "P8BRrje5Bj",
	secret = "6b4b358ffa5169f140c971f035033cd14c9ac5f1ebed4a3be65b7eeaa15b6fc7",
	version = "1.0",
	hash_to_check = getchecksum()
)
'''

key = input("Enter your licence key: ")
keyauthapp.license(key)

instagram_username = input("Enter instagram username: ")
instagram_password = input("Enter instagram password: ")
def make_video():
	clip = VideoFileClip("video/data/background.mp4")

	rand_time = randint(0,500)
	max_time = rand_time + 50

	clip = clip.subclip(rand_time,max_time)
	#clip.preview(fps = 20)
	clip.write_videofile(
        "video/data/temp/temp.mp4",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        threads=multiprocessing.cpu_count(),
    )

	#image1 = (ImageClip(""))

	video = mp.VideoFileClip("video/data/temp/temp.mp4")
	img = (mp.ImageClip("./0.jpeg")
		.set_duration(10)
		.resize(height=720)
		.margin(right=8, top=8, opacity=0)
		.set_pos(("center")))
	final = mp.CompositeVideoClip([video,img])
	img2 = (mp.ImageClip("./1.jpeg")
		.set_start(10)
		.set_duration(10)
		.resize(height=720)
		.margin(right=8, top=8, opacity=0)
		.set_pos(("center")))
	final1 = mp.CompositeVideoClip([final,img2])
	img3 = (mp.ImageClip("./2.jpeg")
		.set_start(20)
		.set_duration(10)
		.resize(height=720)
		.margin(right=8, top=8, opacity=0)
		.set_pos(("center")))
	final2 = mp.CompositeVideoClip([final1,img3])
	img4 = (mp.ImageClip("./3.jpeg")
		.set_start(30)
		.set_duration(10)
		.resize(height=720)
		.margin(right=8, top=8, opacity=0)
		.set_pos(("center")))
	final3 = mp.CompositeVideoClip([final2,img4])
	img5 = (mp.ImageClip("./4.jpeg")
		.set_start(40)
		.set_duration(10)
		.resize(height=720)
		.margin(right=8, top=8, opacity=0)
		.set_pos(("center")))
	final4 = mp.CompositeVideoClip([final3,img5])
	final4.write_videofile("test.mp4")


def run():
    for i in range(0,6):
        res = requests.get("https://meme-api.herokuapp.com/gimme/meme").json()
        RedDownloader.Download(res['postLink'],output=str(i))



def upload_yt():
	from simple_youtube_api.Channel import Channel
	from simple_youtube_api.LocalVideo import LocalVideo

	# loggin into the channel
	channel = Channel()
	channel.login("client_secret.json", "credentials.storage")

	# setting up the video that is going to be uploaded
	video = LocalVideo(file_path="test.mp4")

	# setting snippet
	video.set_title("Memes compilation with Minecraft background! xD")
	video.set_description("Memes from reddit compiled into a video.Every day multiple video,like and subscribe.")
	video.set_tags(["reddit", "memes","funny","xd","funnyvideos","funnymemes","fun"])
	video.set_category("gaming")
	video.set_default_language("en-US")

	# setting status
	video.set_embeddable(True)
	video.set_license("creativeCommon")
	video.set_privacy_status("public")
	video.set_public_stats_viewable(True)

	# setting thumbnail
	video.set_thumbnail_path('1.jpeg')

	# uploading video and printing the results
	video = channel.upload_video(video)
	print(video.id)
	print(video)
	
def upload_ig():
	from instagrapi import Client
	
	cl = Client()
	u = instagram_username
	p = instagram_password
	cl.login(u, p)


	media = cl.clip_upload(
	    "test.mp4",
	    "Memes compilation with Minecraft background #meme #memes #fun #funny #like #comment #follow #like4like #follow4follow #funnypage #memepage #memespage",
	    "video/data/tumb.jpg",
	    extra_data={
	        "custom_accessibility_caption": "alt text example",
	        "like_and_view_counts_disabled": 0,
	        "disable_comments": 0,
	    }
	)
	

while True:
	try:
		run()
		make_video()
		upload_ig()
		#upload_yt()
		print("Uploaded 1 video,waiting 3500s before uploading another video :d")
		sleep(3500)
	except:
		print("errors suck,making new video")
		continue
