from pytube import YouTube
link =input("link")
yt = YouTube(link)
metadat = yt.metadata
print(type(metadat))
print(metadat)