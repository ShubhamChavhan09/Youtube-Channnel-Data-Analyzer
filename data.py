import pandas as pd
import json

def main(file):
    data = None
    with open(file, 'r')as f:
        data = json.load(f)

    channel_id, stats = data.popitem()
    #print(channel_id)
    channel_stats = stats["channel_statistics"]
    video_stats = stats["video_data"]

    #channel statistics
    print(file.replace(".json", ""))
    print('views:', channel_stats["viewCount"])
    print('subscriber:', channel_stats["subscriberCount"])
    print('videos:', channel_stats["videoCount"])

    #video statistics
    sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
    stats = []
    for vid in sorted_vids:
        video_id = vid[0]
        Title = vid[1]["title"]
        views = int(vid[1]["viewCount"])
        likes = int(vid[1]["likeCount"])
        comments =int(vid[1]["commentCount"])
        dislikes = int(vid[1]["dislikeCount"])
        stats.append([Title, views, likes, comments, dislikes])


    df = pd.DataFrame(stats, columns=["Title","views", "likes", "comments", "dislikes"])
    print(df.head(10))

    df.head(10).to_csv('result.csv')

