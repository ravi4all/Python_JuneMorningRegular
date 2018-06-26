import urllib.request

def downloadMp3(url):
    urllib.request.urlretrieve(url,"music_1.mp3")
    print("Downloaded")

downloadMp3("https://downpwnew.com/11985/01%20Jiyo%20Re%20Bahubali%20-%20Bahubali%202%20-%20190Kbps.mp3")
