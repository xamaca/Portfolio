from pytube import YouTube
from sys import argv

links = argv[1]
yt = YouTube(links)

print("title: ", yt.title)
print("views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/faniarodriguez/Desktop/python')
