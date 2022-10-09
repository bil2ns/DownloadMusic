from pytube import YouTube, Playlist, Search

#MP4 İle İndirme
def VideoIndir(link):
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
    
    stream = yt.streams.get_by_itag(22)
    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
    print(f"{songname} başarıyla indirildi")
def playlistVideoIndir(link):
    playlist = Playlist(link)
    print(f"{playlist.title} adlı playlist indiriliyor")
    songnumber = len(playlist.video_urls)
    print(f"Toplamda {songnumber} video bulunmakta")
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
        print(f'{songname} adlı video indiriliyor')
        stream = video.streams.get_by_itag(22)
        stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
        print(f"{songname} adlı video indirildi")
        print("----------------------------------------------------------------------------------")
def arananVideoyuIndir(link):
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
    stream = yt.streams.get_by_itag(22)
    stream.download("C:/Users/clskn/Music/Download", filename=f"{songname}.mp4")
    print(f"{songname} başarıyla indirildi")


#MP3 İle İndirme İşlemleri
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





#Veri Girişleri
url = input("Şarkının linkini ya da ismini giriniz:")
tov =int(input("Video olarak indirmek için 1'i şarkı olarak indirmek için 2'yi tuşlayın'"))
playlistDedector = url.find("playlist")
linkDedector = url.find("http")








#Karar Mekanizması
if playlistDedector == -1 and linkDedector != -1 and tov==2:
    sarkiIndir(url)
elif playlistDedector != -1 and  tov==2:
    playlistIndir(url)
elif playlistDedector == -1 and linkDedector == -1 and  tov==2:
    arananSarkiyiIndir(url)
elif playlistDedector == -1 and linkDedector != -1 and tov==1:
    VideoIndir(url)
elif playlistDedector != -1 and  tov==1:
    playlistVideoIndir(url)
elif playlistDedector == -1 and linkDedector == -1 and  tov==1:
    arananVideoyuIndir(url)

 #ToDo
#Settings kısmını ayarla
#MetaData Olayı
#Grafik Arayüzü
#Kalite Seçimi
#

