from pytube import YouTube, Playlist, Search

#MP4 İle İndirme
def sarkiIndir4(link):
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
    stream = yt.streams.first()

    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
    print(f"{songname} başarıyla indirildi")
def playlistIndir4(link):
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
        video.streams.first().download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
        print(f"{songname} adlı şarkı indirildi")
        print("----------------------------------------------------------------------------------")
def arananSarkiyiIndir4(link):
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
    stream = yt.streams.first()
    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
    print(f"{songname} başarıyla indirildi")


#MP3 İle İndirme İşlemleri
def sarkiIndir3(link):
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
def playlistIndir3(link):
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
def arananSarkiyiIndir3(link):
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





#Veri Girişleri
url = input("Şarkının linkini ya da ismini giriniz:")
tov =int(input("Video olarak indirmek için 1'i şarkı olarak indirmek için 2'yi tuşlayın'"))
pldedector = url.find("playlist")
linkdedector = url.find("http")








#Karar Mekanizması
if pldedector == -1 and linkdedector != -1 and tov==2:
    sarkiIndir3(url)
elif pldedector != -1 and  tov==2:
    playlistIndir3(url)
elif pldedector == -1 and linkdedector == -1 and  tov==2:
    arananSarkiyiIndir3(url)
elif pldedector == -1 and linkdedector != -1 and tov==1:
    sarkiIndir4(url)
elif pldedector != -1 and  tov==1:
    playlistIndir4(url)
elif pldedector == -1 and linkdedector == -1 and  tov==1:
    arananSarkiyiIndir4(url)

#ToDo
#Settings kısmını ayarla
#
#
#
#