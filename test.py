import datetime

currnet_date = datetime.datetime.now()
yesterday = currnet_date - datetime.timedelta(weeks=1)

print(currnet_date, type(currnet_date))
print(yesterday)



# import time
# import asyncio
#
#
#
# async def download_photo(photo_count, limit):
#     while photo_count < limit:
#         await asyncio.sleep(1)
#         photo_count += 1
#         print(f"Photo {photo_count}")
#
#
#
# async def download_video(video_count, limit):
#     while video_count < limit:
#         await asyncio.sleep(5)
#         video_count += 1
#         print(f"Video {video_count}")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count, 10),
#         download_video(video_count, 3)
#     ]
#     await asyncio.gather(*task_list)
#
#
# asyncio.run(main())




# def test(a: int) -> None:
#     return str(a)
#
# a = test(a)