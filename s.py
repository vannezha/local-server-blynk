from playsound import playsound
import time

def playmusic(music):
    playsound(music)
def returntime(arrsetTime):
    return arrsetTime[0] * 3600 + arrsetTime[1] * 60 + arrsetTime[2]

belPertama = [6, 45, 0]
belKedua = [7, 0, 0]
belKetiga = [7, 40, 0]
belKeempat = [8, 20, 0]
belKelima = [9, 0, 0]
belKeenam = [9, 40, 0]
belKeTujuh = [9, 55, 0]
belKeDelapan = [10, 35, 0]
belKeSembilan = [11, 15, 0]
belKeSepuluh = [11, 55, 0]
belKeSebelas = [12, 45, 0]
belKeDuabelas = [13, 25, 0]
belKeTigabelas = [14, 5, 0]
belKeEmpatbelas = [15, 0, 0]

# bikin code tentang jadwal dan upload file music
# yg bisa dicustome waktunya
# perintah on off ampli lewat komunikasi serial
hour = time.localtime(round(time.time())).tm_hour
minute = time.localtime(round(time.time())).tm_min
second = time.localtime(round(time.time())).tm_sec
nowTime = hour * 3600 + minute * 60 + second

if(nowTime >= returntime(belPertama) and nowTime < returntime(belKedua)):
    # bel pertama
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKedua) and nowTime < returntime(belKetiga)):
    # bel kedua
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKetiga) and nowTime < returntime(belKeempat)):
    # bel ketiga
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeempat) and nowTime < returntime(belKelima)):
    # bel keempat
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKelima) and nowTime < returntime(belKeenam)):
    # bel kelima
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeenam) and nowTime < returntime(belKeTujuh)):
    # bel keenam
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeTujuh) and nowTime < returntime(belKeDelapan)):
    # bel ke tujuh
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeDelapan) and nowTime < returntime(belKeSembilan)):
    # bel ke delapan
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeSembilan) and nowTime < returntime(belKeSepuluh)):
    # bel ke sembilan
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeSepuluh) and nowTime < returntime(belKeSebelas)):
    # bel ke sepuluh
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeSebelas) and nowTime < returntime(belKeDuabelas)):
    # bel ke duabelas
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeDuabelas) and nowTime < returntime(belKeTigabelas)):
    # bel ke tigabelas
    playmusic("music/1.mp3")
elif(nowTime >= returntime(belKeTigabelas) and nowTime < returntime(belKeEmpatbelas)):
    # bel ke empatbelas
    playmusic("music/1.mp3")
else:
    # bel ke empatbelas
    playmusic("music/1.mp3")