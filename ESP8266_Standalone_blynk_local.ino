#define BLYNK_PRINT Serial

/* Fill in information from Blynk Device Info here */
#define BLYNK_TEMPLATE_ID           "vannezha"
#define BLYNK_TEMPLATE_NAME         "vannezha-bel-muhi"
#define BLYNK_AUTH_TOKEN            "z296MHR9tEHFoR4i3dbWwRLypIpmGcOs"


#include <WiFiUdp.h>
#include <NTPClient.h>
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 3600*7);

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Leslesan Baruuuuuuuuu";
char pass[] = "Vivattttt";

// ipserver and port address
int ipA = 192 , ipB = 168 , ipC = 68 , ipD = 106 , port = 8082 ;
int jam1 = 0 , jam2 = 0 , jam3 = 0 , jam4 = 0 ,jam5 = 0 , jam6 = 0 ,jam7 = 0 , jam8 = 0 ,jam9 = 0 , jam10 = 0 ,jam11 = 0 , jam12 = 0 ,jam13 = 0 , jam14 = 0 ;

int waktuServer;

void pergantianJAM();

void setup()
{
  // Debug console
  Serial.begin(9600);
  timeClient.begin();
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass, IPAddress(ipA, ipB, ipC, ipD), port);
}

void loop()
{
  Blynk.run();
  timeClient.update();
  pergantianJAM();
}

void pergantianJAM(){
  Serial.println(timeClient.getFormattedTime());
  waktuServer = timeClient.getHours() * 3600 + timeClient.getMinutes() * 60 + timeClient.getSeconds() ;
  
  if(waktuServer >= jam1 && waktuServer < jam2){
    // bel jam pertama
  }elseif(waktuServer >= jam2 && waktuServer < jam3){
    // bel jam kedua
  }elseif(waktuServer >= jam3 && waktuServer < jam4){
    // bel jam ketiga
  }elseif(waktuServer >= jam4 && waktuServer < jam5){
    // bel jam keempat
  }elseif(waktuServer >= jam5 && waktuServer < jam6){
    // bel jam kelima
  }elseif(waktuServer >= jam6 && waktuServer < jam7){
    // bel jam keenam
  }elseif(waktuServer >= jam7 && waktuServer < jam8){
    // bel jam ketujuh
  }elseif(waktuServer >= jam8 && waktuServer < jam9){
    // bel jam kedelapan
  }elseif(waktuServer >= jam9 && waktuServer < jam10){
    // bel jam kesembilan
  }elseif(waktuServer >= jam10 && waktuServer < jam11){
    // bel jam kesepuluh
  }elseif(waktuServer >= jam11 && waktuServer < jam12){
    // bel jam kesebelas
  }elseif(waktuServer >= jam12 && waktuServer < jam13){
    // bel jam keduabelas
  }elseif(waktuServer >= jam13 && waktuServer < jam14){
    // bel jam terakhir
  }elseif(waktuServer >= jam14){
    // reset
  }

  Serial.println(waktuServer);
  Serial.println(waktuServer % 5);
  
  delay(1000);
}

BLYNK_WRITE(V0)
{
  int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
  // You can also use:
  // String i = param.asStr();
  // double d = param.asDouble();
  Serial.print("V0 value is: ");
  Serial.println(pinValue);
}

BLYNK_WRITE(V1)
{
  int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
  // You can also use:
  // String i = param.asStr();
  // double d = param.asDouble();
  Serial.print("V1 value is: ");
  Serial.println(pinValue-1);
}

// get value of jam1 
BLYNK_WRITE(V2){jam1 = param.asInt();}

// get value of jam2 
BLYNK_WRITE(V3){jam2 = param.asInt();}

// get value of jam3 
BLYNK_WRITE(V4){jam3 = param.asInt();}

// get value of jam4 
BLYNK_WRITE(V5){jam4 = param.asInt();}

// get value of jam5 
BLYNK_WRITE(V6){jam5 = param.asInt();}

// get value of jam6 
BLYNK_WRITE(V7){jam6 = param.asInt();}

// get value of jam7 
BLYNK_WRITE(V8){jam7 = param.asInt();}

// get value of jam8 
BLYNK_WRITE(V9){jam8 = param.asInt();}

// get value of jam9 
BLYNK_WRITE(V10){jam9 = param.asInt();}

// get value of jam10 
BLYNK_WRITE(V11){jam10 = param.asInt();}

// get value of jam11 
BLYNK_WRITE(V12){jam11 = param.asInt();}

// get value of jam12 
BLYNK_WRITE(V13){jam12 = param.asInt();}

// get value of jam13 
BLYNK_WRITE(V14){jam13 = param.asInt();}


