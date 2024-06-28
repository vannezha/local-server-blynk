from playsound import playsound
from serial import Serial
import time

ser = Serial('COM6', 9600, timeout=1)

def playmusic(music):
    playsound(music)
def returntime(arrsetTime):
    return arrsetTime[0] * 3600 + arrsetTime[1] * 60 + arrsetTime[2]
def micAmpli(command):
    ser.write(command.encode())
    time.sleep(3)
    # return ser.readlines()

ON = '1'
OFF = '0'

sudahBel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
belKeTigabelas = [18, 5, 0]
belKeEmpatbelas = [21, 0, 0]

# bikin code tentang jadwal dan upload file music
# yg bisa dicustome waktunya
# perintah on off ampli lewat komunikasi serial
hour = time.localtime(round(time.time())).tm_hour
minute = time.localtime(round(time.time())).tm_min
second = time.localtime(round(time.time())).tm_sec
nowTime = hour * 3600 + minute * 60 + second

while(True):
    with open("data.txt", "r") as f:
        data = eval(str(f.readlines()[0]))

    if(nowTime >= returntime(belPertama) and nowTime < returntime(belKedua)):
        # bel pertama
        if data[0] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[0] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKedua) and nowTime < returntime(belKetiga)):
        # bel kedua
        if data[1] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[1] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKetiga) and nowTime < returntime(belKeempat)):
        # bel ketiga
        if data[2] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[2] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeempat) and nowTime < returntime(belKelima)):
        # bel keempat
        if data[3] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[3] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKelima) and nowTime < returntime(belKeenam)):
        # bel kelima
        if data[4] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[4] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeenam) and nowTime < returntime(belKeTujuh)):
        # bel keenam
        if data[5] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[5] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeTujuh) and nowTime < returntime(belKeDelapan)):
        # bel ke tujuh
        if data[6] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[6] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeDelapan) and nowTime < returntime(belKeSembilan)):
        # bel ke delapan
        if data[7] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[7] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeSembilan) and nowTime < returntime(belKeSepuluh)):
        # bel ke sembilan
        if data[8] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[8] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeSepuluh) and nowTime < returntime(belKeSebelas)):
        # bel ke sepuluh
        if data[9] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[9] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeSebelas) and nowTime < returntime(belKeDuabelas)):
        # bel ke sebelas
        if data[10] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[10] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeDuabelas) and nowTime < returntime(belKeTigabelas)):
        # bel ke duabelas
        if data[11] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[11] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    elif(nowTime >= returntime(belKeTigabelas) and nowTime < returntime(belKeEmpatbelas)):
        # bel ke tigabelas
        if data[12] == 0:
            micAmpli(ON)
            playmusic("music/1.mp3")
            micAmpli(OFF)
            data[12] = 1
            with open("data.txt", "w") as f:
                f.write(str(data))
    else:
        # reset bel
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        with open("data.txt", "w") as f:
            f.write(str(data))