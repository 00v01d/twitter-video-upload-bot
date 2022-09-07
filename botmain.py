import tweepy
import time
import os

consumer_key = "add key here"
consumer_secret = "add key here"

key = "add key here"
secret = "add key here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


def upload_media(text,filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

def main():
  try:
   upload_media(" ","video.mp4")
   print("Media was uploaded!!")
   os.remove("video.mp4")
   main()
  except:
   print("Media was not uploaded!!")
   time.sleep(1)
   main()
main()