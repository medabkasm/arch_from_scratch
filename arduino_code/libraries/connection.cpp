#include "Arduino.h"
#include"connection.h"
#include"sensors.h"

bool init_SAP(const char* ssid,IPAddress local_IP,IPAddress gateway,IPAddress subnet){

  Serial.print("Setting soft-AP configuration ... ");
  if(WiFi.softAPConfig(local_IP,gateway,subnet)){
    Serial.println("Ready");
    Serial.println("Setting soft-AP ... ");
    if(WiFi.softAP(ssid,false)){
      Serial.println("Ready");
      Serial.print("Soft-AP IP address : ");
      Serial.println(WiFi.softAPIP());
      return true;
    }
    else{
      Serial.println("Failed setting UP AP");
      return false;
    }
  }
  else{
    Serial.println("Failed configuring AP");
    return false;
  }

}

bool init_station(const char* ssid,const char* password,IPAddress staticIp,IPAddress gateway,IPAddress subnet ){
  Serial.printf("Connecting to %s\n", ssid);
  if(WiFi.config(staticIp, gateway, subnet)){
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED){
      Serial.printf("waiting for connection ...\n");
      delay(1000);
    }
    Serial.print("Connected, IP address : ");
    Serial.println(WiFi.localIP());
    return true;
  }

  return false;
}

bool Connection::timeout(WiFiClient client,unsigned long maxTime){
  unsigned long startTime = millis();
  while(!client.available()){
    if(millis() - startTime > maxTime ){
      Serial.println("connection timeout , connection with the server will be closed");
      return true ;
    }
  }
  return false;
}

bool Connection::init_connection(WiFiClient client,unsigned long maxTime){

  Serial.println("client connected"); // start connection with the server
  client.print("STR");

  if(timeout(client,maxTime)){
    client.stop();
    return false;
  }
  String response  = client.readStringUntil('\r');
  if(response == "STR"){
    Serial.println("start handshake...");
    client.print("EST"); // connection is established , confirmed to the server with EST (established) flag
    Serial.println("Connection with the server is established");
    return true;
    }
    else{
      Serial.println("FLAG :: "+response+" :: bad flag , connection with the server will be closed");
      client.stop();
      return false;
    }

}

void Connection::get_command(WiFiClient client , unsigned long maxTime , unsigned short orderPin){

  if(timeout(client,maxTime)){
    client.stop();
    return;
  }

  String response = client.readStringUntil('\r');
  if (response == "EXC"){ // order flag
    Serial.println("action begins");
  //  executes the function that is responsible for actuator's command execution (pompe , electro valve)
    Serial.println("order executed");
    client.print("CNF"); // confirm flag
    Serial.println("confirming order to the server...");

    if(timeout(server,maxTime)){
      Serial.println("order not confirmed");
      client.stop();
      return;
    }
    response = client.readStringUntil('\r');
    if (response == "RECV"){
      Serial.println("order confirmed");
    }
    else{
      Serial.println("FLAG :: "+response+" :: bad flag , connection with the server will be closed");
    }
    delay(2000);
    client.stop();
  }
  else{
    Serial.println("FLAG :: "+response+" :: bad flag , connection with the server will be closed");
    client.stop();
  }

}
