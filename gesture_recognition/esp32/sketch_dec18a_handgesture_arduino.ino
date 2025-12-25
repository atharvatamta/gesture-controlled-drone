#include <WiFi.h>
#include <WiFiUdp.h>
//wifi
const char* ssid = "iPhone";
const char* password = "dzvt7934";

//UDP 
WiFiUDP udp;
const int UDP_PORT = 5005;
char packet[64];
//Motor connection
const int M1 = 3;   // Motor 1
const int M2 = 4;   // Motor 2
const int M3 = 5;   // Motor 3
const int M4 = 6;   // Motor 4

//pwm
const int PWM_FREQ = 20000;   // 20 kHz for brushed motors
const int PWM_RES  = 8;       // 0–255

//control
int baseThrottle = 0;         // motors OFF by default
unsigned long lastCmdTime = 0;

//helper
int clamp(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

void setMotors(int a, int b, int c, int d) {
  ledcWrite(M1, clamp(a, 0, 255));
  ledcWrite(M2, clamp(b, 0, 255));
  ledcWrite(M3, clamp(c, 0, 255));
  ledcWrite(M4, clamp(d, 0, 255));
}

//hard cutoff -> stop
void stopMotors() {
  baseThrottle = 0;
  setMotors(0, 0, 0, 0);
  Serial.println("STOP: MOTORS OFF");
}

void setup() {
  Serial.begin(115200);

  // Attach PWM
  ledcAttach(M1, PWM_FREQ, PWM_RES);
  ledcAttach(M2, PWM_FREQ, PWM_RES);
  ledcAttach(M3, PWM_FREQ, PWM_RES);
  ledcAttach(M4, PWM_FREQ, PWM_RES);

  // 🔒FORCE MOTORS OFF AT BOOT
  stopMotors();
  delay(200);

  // WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());

  udp.begin(UDP_PORT);
  Serial.println("LITEWING BASIC MOTOR CONTROL READY");
}

void loop() {

  //failsafe no commands 
  if (millis() - lastCmdTime > 1000) {
    stopMotors();
  }

  // udp
  int size = udp.parsePacket();
  if (!size) return;

  int len = udp.read(packet, sizeof(packet) - 1);
  packet[len] = 0;
  String cmd = String(packet);

  lastCmdTime = millis();

  if (cmd == "START") {
    baseThrottle = 80;   // safe start value
    setMotors(baseThrottle, baseThrottle, baseThrottle, baseThrottle);
  }
  else if (cmd == "UP") {
    baseThrottle = clamp(baseThrottle + 10, 0, 150);
    setMotors(baseThrottle, baseThrottle, baseThrottle, baseThrottle);
  }
  else if (cmd == "DOWN") {
    baseThrottle = clamp(baseThrottle - 10, 0, 150);
    setMotors(baseThrottle, baseThrottle, baseThrottle, baseThrottle);
  }
  else if (cmd == "STOP") {
    stopMotors();   // FULL SHUTDOWN
  }

  Serial.print("CMD: ");
  Serial.print(cmd);
  Serial.print(" | baseThrottle=");
  Serial.println(baseThrottle);
}