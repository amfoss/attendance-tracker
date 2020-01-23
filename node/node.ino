#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <time.h>
#include <Ticker.h>
#include <EEPROM.h>

#define ull unsigned long long

Ticker blinker;
ESP8266WebServer server(80);

const char* password
char ssid[100];
ull a, c, m, addr;

ull change_seed(ull seed) {
  seed = (seed % m) * (a % m);
  seed = seed % m;
  seed += c;
  seed %= m;
  return seed;
}

ull get_seed() {
  ull seed;
  EEPROM.get(addr, seed);
  return seed;
}

void write_seed(ull seed){
  EEPROM.put(addr, seed);
  EEPROM.commit();
}

void changeWifi() {
  ull seed = get_seed();
  seed = change_seed(seed);
  write_seed(seed);  
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
}

void setup() {
  delay(1000);
  Serial.begin(115200);
  EEPROM.begin(512);
  Serial.println("Initial Setup");
  ull seed = get_seed();
  sprintf(ssid, "amFOSS_%d", seed);
  WiFi.softAP(ssid, password);
  Serial.println(ssid);
  Serial.println(WiFi.softAPIP());
  server.on("/reset", HTTP_GET, reset_EEPROM);
  server.begin();
  blinker.attach(300, changeWifi);
}

void reset_EEPROM(){
  Serial.println("RESETTING");
  blinker.detach();
  EEPROM.put(addr, 1000);
  String response = "<!DOCTYPE html>\n";
  response += "<html>\n";
  response += "<head>\n";
  response += "<title>Wifi Control Page</title>\n";
  response += "</head>\n";
  response += "<body>\n";
  response += "<h1>Node Status</h1>\n";
  response += "<p>EEPROM seed set to 1000</p>\n";
  response += "</body>\n";
  response += "</html>\n";
  server.send(200, "text/html", response);
  delay(1000);
  changeWifi();
  blinker.attach(300, changeWifi);
}

void loop() {
  server.handleClient();
}
