from pytube import YouTube, Playlist, Search

def sarkiIndir(link):
    yt = YouTube(link)
    songname = yt.title
    author = yt.author
    songname = songname.replace("/", " ")  #
    songname = songname.replace("|", " ")  #
    songname = songname.replace("*", " ")  #
    songname = songname.replace("<", " ")  # Bu kısımda kaydedilemeyecek sembolleri çıkarıyor
    songname = songname.replace(">", " ")  #
    songname = songname.replace(":", " ")  #
    songname = songname.replace("?", " ")  #
    songname = songname.replace('"', " ")  #

    print(f"{songname} indiriliyor...")
    stream = yt.streams.filter(only_audio=True).first()

    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp3")
    print(f"{songname} başarıyla indirildi")
def playlistIndir(link):
    playlist = Playlist(link)
    print(f"{playlist.title} adlı playlist indiriliyor")
    songnumber = len(playlist.video_urls)
    print(f"Toplamda {songnumber} şarkı bulunmakta")
    print("----------------------------------------------------------------------------------")
    for video in playlist.videos:
        songname= video.title
        songname = songname.replace("/", " ")#
        songname = songname.replace("|", " ")#
        songname = songname.replace("*", " ")#
        songname = songname.replace("<", " ")#Bu kısımda kaydedilemeyecek sembolleri çıkarıyor
        songname = songname.replace(">", " ")#
        songname = songname.replace(":", " ")#
        songname = songname.replace("?", " ")#
        songname = songname.replace('"', " ")#
        print(f'{songname} adlı şarkı indiriliyor')
        video.streams.filter(only_audio=True)
        video.streams.first().download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp3")
        print(f"{songname} adlı şarkı indirildi")
        print("----------------------------------------------------------------------------------")
def arananSarkiyiIndir(link):
    s = Search(link)
    ytid = str(s.results[0])
    directid = ytid.find("=") + 1
    ytid = ytid[directid:]
    song = "https://youtu.be/" + ytid

    yt = YouTube(song)
    songname = yt.title
    author = yt.author
    songname = songname.replace("/", " ")  #
    songname = songname.replace("|", " ")  #
    songname = songname.replace("*", " ")  #
    songname = songname.replace("<", " ")  # Bu kısımda kaydedilemeyecek sembolleri çıkarıyor
    songname = songname.replace(">", " ")  #
    songname = songname.replace(":", " ")  #
    songname = songname.replace("?", " ")  #
    songname = songname.replace('"', " ")  #
    print(f"{songname} indiriliyor...")
    stream = yt.streams.filter(only_audio=True).first()
    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp3")
    print(f"{songname} başarıyla indirildi")



url = input("Şarkının linkini ya da ismini giriniz:")
pldedector = url.find("playlist")
linkdedector = url.find("http")

 #Şarkı ile playlisti ayırt etmeye yarar
if pldedector == -1 and linkdedector != -1:
    sarkiIndir(url)
elif pldedector != -1:
    playlistIndir(url)
elif pldedector == -1 and linkdedector == -1:
    arananSarkiyiIndir(url)

