
#ifndef CONNECTION_H
#define CONNECTION_H

#include "Arduino.h"
#include <ESP8266WiFi.h>


bool init_SAP(String ssid,IPAddress local_IP,IPAddress gateway,IPAddress subnet);
bool init_station(const char* ssid,const char* password,IPAddress staticIp,IPAddress gateway,IPAddress subnet);

class Connection{
  private:
    bool timeout(WiFiClient client,unsigned long maxTime);
  public:
    bool init_connection(WiFiClient client,unsigned long maxTime);
    void get_command(WiFiClient client ,unsigned long maxTime);
};

#endif
