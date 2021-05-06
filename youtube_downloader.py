from pytube import YouTube

print("Enter the url of the video:")

url = input()

yt = YouTube(url)

# Youtube video title
print(f"Title:  {yt.title}")

# # video thumbnail
# print(yt.thumbnail_url)

sl = 0
record_res = {}

# all stream resolutions
for stream in yt.streams:
    sl+=1
    print(f"{sl} -- {stream.resolution}")
    record_res[sl] = stream.resolution

Selected_resol = input("Enter the no for which the resolution you want to download: ")


# downloading the video in desired resoultion
down_vid = yt.streams.filter(res=Selected_resol)
down_vid.first().download()

print("\nDownload Completed...")