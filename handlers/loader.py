# from pytube import YouTube
# import uuid
#
#
# def download_video(url):
#     yt = YouTube(url)
#     video_id = uuid.uuid4().fields[-1]
#     yt.streams.filter(only_video=True).first().download(
#         "..media.video", f"{video_id}.mp4"
#     )
#     return f"{video_id}.mp4"
#
#
# download_video("https://www.youtube.com/watch?v=PoN05pqAtz4&pp=ygUMdmlkZW8gMzAgc2Vj")