from youtube_statistics import YTstats
from data import main


API_KEY = input("Enter API Key:")
channel_id = input("Enter the channel ID :")
print("Please wait...")

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
file_name = yt.dump()
main(file_name)



