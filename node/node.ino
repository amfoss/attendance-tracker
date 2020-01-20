#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <time.h>
#include <Ticker.h>
#include <EEPROM.h>

Ticker blinker;

const char* password = "";
char ssid[100];
unsigned int addr = 0;
unsigned long long a, c, m, seed;

void change_seed() {
  seed = (seed % m) * (a % m);
  seed = seed % m;
  seed += c;
  seed %= m;
}

void get_seed() {
  EEPROM.get(addr, seed);
  Serial.print("current seed changed in EEPROM");
  if (seed == NULL){
    seed = 1000;
    EEPROM.put(addr, seed);
    EEPROM.commit();
  }
}

void changeWifi() {
  change_seed();
  EEPROM.put(addr, seed);
  EEPROM.commit();
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
}

void setup() {
  delay(1000);
  Serial.begin(115200);
  EEPROM.begin(512);
  Serial.print("Initial Setup");
  get_seed();
  change_seed();
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
  blinker.attach(300, changeWifi);
}

void loop() {
}
