import moviepy
import moviepy.editor as mp
from moviepy.editor import *
from random import randint
import multiprocessing


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
