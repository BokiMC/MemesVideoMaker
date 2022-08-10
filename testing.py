from keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime


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


key = input("Enter your licence key: ")
keyauthapp.license(key)