from playsound import playsound
from serial import Serial
import time

try:
    with open("data.txt", "r") as f:
        port = str(f.readline())
except:
    port = "COM5"

ser = Serial('COM5', 9600, timeout=1)

sleepbefore = 5
sleepafter = 3

def playmusic(music):
    playsound(music)
def returntime(arrsetTime):
    return arrsetTime[0] * 3600 + arrsetTime[1] * 60 + arrsetTime[2]
def micAmpli(command, waktu = 10):
    time.sleep(waktu)
    ser.write(command.encode())
    time.sleep(waktu)
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
belKeTigabelas = [14, 5, 0]
belKeEmpatbelas = [15, 0, 0]

# belPertama = [6, 0, 0]
# belKedua = [6, 2, 0]
# belKetiga = [6, 4, 0]
# belKeempat = [6, 6, 0]
# belKelima = [6, 8, 0]
# belKeenam = [6, 10, 0]
# belKeTujuh = [6, 12, 0]
# belKeDelapan = [6, 14, 0]
# belKeSembilan = [6, 16, 0]
# belKeSepuluh = [6, 18, 0]
# belKeSebelas = [6, 20, 0]
# belKeDuabelas = [6, 22, 0]
# belKeTigabelas = [6, 24, 0]
# belKeEmpatbelas = [6, 26, 0]

musikBelPertama = "music\segera memasuki masjid.mp3"
musikBelKedua = "music\jam pertama.mp3"
musikBelKetiga = "music\jam ke 2.mp3"
musikBelKeempat = "music\jam ke 3.mp3"
musikBelKelima = "music\jam-ke-4_1.mp3"
musikBelKeenam = "music\istirahat_1.mp3"
musikBelKetujuh = "music\jam-ke5.mp3"
musikBelKedelapan = "music\jam ke 6.mp3"
musikBelKesembilan = "music\jam ke 7.mp3"
musikBelKesepuluh = "music\solat.mp3"
musikBelKesebelas = "music\jam ken 8.mp3"
musikBelKeduabelas = "music\jam ken 9.mp3"
musikBelKetigabelas = "music\pulang.mp3"
musikBelKeempatbelas = "music\pulang.mp3"

# bikin code tentang jadwal dan upload file music
# yg bisa dicustome waktunya
# perintah on off ampli lewat komunikasi serial


while(True):
    try:
        hour = time.localtime(round(time.time())).tm_hour
        minute = time.localtime(round(time.time())).tm_min
        second = time.localtime(round(time.time())).tm_sec
        nowTime = hour * 3600 + minute * 60 + second
        
        with open("data.txt", "r") as f:
            data = eval(str(f.readlines()[0]))

        if(nowTime >= returntime(belPertama) and nowTime < returntime(belKedua)):
            # bel pertama
            if data[0] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelPertama)
                micAmpli(OFF, sleepafter)
                data[0] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKedua) and nowTime < returntime(belKetiga)):
            # bel kedua
            if data[1] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKedua)
                micAmpli(OFF, sleepafter)
                data[1] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKetiga) and nowTime < returntime(belKeempat)):
            # bel ketiga
            if data[2] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKetiga)
                micAmpli(OFF, sleepafter)
                data[2] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeempat) and nowTime < returntime(belKelima)):
            # bel keempat
            if data[3] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKeempat)
                micAmpli(OFF, sleepafter)
                data[3] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKelima) and nowTime < returntime(belKeenam)):
            # bel kelima
            if data[4] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKelima)
                micAmpli(OFF, sleepafter)
                data[4] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeenam) and nowTime < returntime(belKeTujuh)):
            # bel keenam
            if data[5] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKeenam)
                micAmpli(OFF, sleepafter)
                data[5] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeTujuh) and nowTime < returntime(belKeDelapan)):
            # bel ke tujuh
            if data[6] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKetujuh)
                micAmpli(OFF, sleepafter)
                data[6] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeDelapan) and nowTime < returntime(belKeSembilan)):
            # bel ke delapan
            if data[7] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKedelapan)
                micAmpli(OFF, sleepafter)
                data[7] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeSembilan) and nowTime < returntime(belKeSepuluh)):
            # bel ke sembilan
            if data[8] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKesembilan)
                micAmpli(OFF, sleepafter)
                data[8] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeSepuluh) and nowTime < returntime(belKeSebelas)):
            # bel ke sepuluh
            if data[9] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKesepuluh)
                micAmpli(OFF, sleepafter)
                data[9] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeSebelas) and nowTime < returntime(belKeDuabelas)):
            # bel ke sebelas
            if data[10] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKesebelas)
                micAmpli(OFF, sleepafter)
                data[10] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeDuabelas) and nowTime < returntime(belKeTigabelas)):
            # bel ke duabelas
            if data[11] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKeduabelas)
                micAmpli(OFF, sleepafter)
                data[11] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        elif(nowTime >= returntime(belKeTigabelas) and nowTime < returntime(belKeEmpatbelas)):
            # bel ke tigabelas
            if data[12] == 0:
                micAmpli(ON, sleepbefore)
                playmusic(musikBelKetigabelas)
                micAmpli(OFF, sleepafter)
                data[12] = 1
                with open("data.txt", "w") as f:
                    f.write(str(data))
                    f.close()
        else:
            # reset bel
            data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            with open("data.txt", "w") as f:
                f.write(str(data))
                f.close()
    except:
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        with open("data.txt", "w") as f:
            f.write(str(data))
            f.close()