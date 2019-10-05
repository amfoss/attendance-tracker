#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <time.h>
#include <Ticker.h>

Ticker blinker;

const char* password = "";
char ssid[100];
unsigned long long a, c, m, seed;
void change_seed(){
  seed = (seed%m) * (a%m);
  seed = seed%m;
  seed += c;
  seed %= m;
}

void changeWifi(){
  change_seed();
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
}

void setup() {
  delay(1000);
  Serial.begin(115200);
  Serial.print("Initial Setup");
  change_seed();
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
  blinker.attach(300, changeWifi);
}

void loop() {
}
