//#include <ESP8266WiFi.h> already included in connection.h file
#include"connection.h"


const char* ssid = "redmi";
const char* password = "";

IPAddress local_IP(192,168,43,6);
IPAddress gateway(192,168,43,11);
IPAddress subnet(255,255,255,0);

WiFiServer server(25);


void setup(void){
  Serial.begin(9600);

  while(true){
    if( init_station(ssid,password,local_IP,gateway,subnet) ){
      server.begin();
      break;
    }
    delay(5000); // wait for 5sec befor trying to reconect to the AP
  }
}

void loop() {

  WiFiClient client = server.available(); // create a new connection with the server
  delay(1000);

  if(client.connected()){

    Connection *node ;
    node = new Connection;

    if(node->init_connection(client,10000)){ // initialise connection between the client and the server (handshake)
      node->get_command(client,10000); // execute the command (actuator) and close connection
      delete node;
    }
  }

}
