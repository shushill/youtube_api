from youtubeapi import settings
import json
import requests
import re
# import googleapiclient.discovery
# import googleapiclient.errors

#from apiclient.discovery import build
import googleapiclient.discovery
from datetime import datetime, timedelta
import apiclient
import os


from youtubeApp.models import VideoDetail








# class Youtube:

#     def __init__(self, *args, **kwargs):
#         self.api_service_name = settings.API_SERVICE_NAME
#         self.api_version = settings.API_VERSION
#         self.developer_key = settings.GOOGLE_API_KEY

#         self.youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, developerKey=self.developer_key)

#     def get_data(self):
#         # try:
#         #     time_now = datetime.now()
#         #     last_request_time = time_now - timedelta(days=1)
#         #     videolist_request = self.youtube.search().list(q="cricket", part="snippet", order="date", maxResults=50, publishedAfter=(last_request_time.replace(microsecond=0).isoformat("T") + "Z"))
#         videolist_request = self.youtube.search().list(q="cricket", part="id,snippet", type='video', maxResults=50,
#                         fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))")
#         result = videolist_request.execute()
#         # except apiclient.errors.HttpError as err:
#         #     code = err.resp.status
#         #     if (code == 400 or code == 403):
#         #         return
#         #print(result)
#         # for item in result["items"]:
#         #     video_id = item["id"]["videoId"]
#         #     # published_at = item['snippet']['publishedAt']
#         #     video_title = item["snippet"]["title"]
#         #     video_desc = item["snippet"]["description"]
#         #     # thumbnail_url = item['snippet']['thumbnails']['default']['url']
#         #     print(video_title)
#         #       VideoDetail.objects.create(video_id=video_id, video_title=video_title, video_desc=video_desc)
#         VideoDetail.objects.create(video_id="12987654", video_title="video_title", video_desc="video_desc")

def get_data(query):
    api_service_name = settings.API_SERVICE_NAME
    api_version = settings.API_VERSION
    developer_key = settings.GOOGLE_API_KEY
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
    videolist_request = youtube.search().list(q=query, part="id,snippet", type='video', maxResults=50, fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))")
    result = videolist_request.execute()
    #print(result)
    for item in result["items"]:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_desc = item["snippet"]["description"]
        VideoDetail.objects.create(video_id=video_id, video_title=video_title, video_desc=video_desc)



def update_something():
    query = "football"
    get_data(query)
    print("running")
