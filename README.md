# Gesture Controlled Drone with Real Time Crowd Detection
![IMG_8816](https://github.com/user-attachments/assets/092f94ae-1abc-4cff-9ff8-93bc28610b73)

## Overview

This project presents a gesture controlled drone system integrated with real time crowd detection and density visualization. The core idea is to use a laptop as a ground control station where hand gestures are recognized and translated into drone commands, while simultaneously processing live video from the drone to analyze crowd density.

The system is designed as a complete solution combining computer vision, deep learning, embedded systems, and wireless communication. It demonstrates how human gestures can be used as an intuitive control interface for drones and how aerial vision can be leveraged for crowd monitoring applications.

<img width="300" height="300" alt="Screenshot 2025-12-19 at 13 48 44" src="https://github.com/user-attachments/assets/4fcfd344-c1e4-478a-9527-8e83021ffbdf" />

<img width="300" height="300" alt="Screenshot 2025-12-19 at 13 50 49" src="https://github.com/user-attachments/assets/3dc37bf3-4cf4-4b24-915a-12eaa3fbf36b" />
<img width="300" height="300" alt="Screenshot 2025-12-19 at 13 33 45" src="https://github.com/user-attachments/assets/34f1b0a0-a9ab-4f90-a5cf-41b43d3d7cca" />
<img width="300" height="300" alt="Screenshot 2025-12-19 at 13 34 18" src="https://github.com/user-attachments/assets/c9d06e42-081e-4de7-adf7-ce9d6f9fe996" />


## System Workflow

<img width="600" height="300" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/4e382f55-0b34-4fc8-b9de-a8b030b85532" />


The laptop acts as the ground station and control hub for the entire system. A webcam connected to the laptop continuously captures hand movements. These hand gestures are detected using MediaPipe Hands, and a custom hand gesture dataset is used to recognize specific control gestures such as takeoff, landing, and directional movement.

Once a gesture is recognized, it is mapped to a corresponding drone command. These commands are transmitted wirelessly to an ESP32-based drone using UDP communication. On the drone side, Arduino firmware running on the ESP32 interprets the received commands and controls the motors accordingly.

The drone is also equipped with an onboard ESP32-S3 camera module. This camera streams live video footage back to the ground control station over Wi-Fi. The incoming video stream is processed in real time using a YOLOv8n model trained on a custom person-only subset of the VisDrone dataset. The model was trained on Google Colab using Ultralytics Hub for efficient experimentation and deployment.

From the detection results, the system continuously computes the number of people present in the scene. A live crowd density heatmap is also generated using Gaussian-based intensity accumulation, giving a visual representation of crowd concentration. The ground station displays the live feed, person count, and heatmap simultaneously, enabling real-time situational awareness.

![Image 22-08-25 at 12 39 (1)](https://github.com/user-attachments/assets/2dcd7ab8-7d0e-4d7e-ab03-b589f07855a5)

![Image 22-08-25 at 12 40](https://github.com/user-attachments/assets/dfabc244-6053-4074-a245-627a39e3c454)

![Image 22-08-25 at 12 39](https://github.com/user-attachments/assets/faf9e581-5b2c-4336-8066-8b46b87b4b14)


## Problem Statement

Traditional drone control systems rely heavily on physical remote controllers, which require training and limit intuitive interaction. Additionally, crowd monitoring using static CCTV cameras provides limited spatial coverage and flexibility.

This project addresses both challenges by introducing a gesture-based drone control mechanism that allows natural human interaction without a physical controller, and by integrating real-time aerial crowd detection and density analysis. The solution is especially relevant for applications such as crowd management, disaster response, public safety monitoring, and smart surveillance systems.



## Components Used

The system is built using a combination of hardware and software components. On the hardware side, an ESP32-based drone controller is used for flight control, along with an ESP32-S3 camera module for live video streaming. A laptop with a webcam functions as the ground control station.

On the software side, MediaPipe Hands is used for hand landmark detection and gesture recognition. Python is used for gesture processing, communication, and crowd analysis. YOLOv8n is employed for person detection, trained on a custom VisDrone persons dataset using Ultralytics Hub. Arduino firmware is used to control the drone motors based on received commands.

<img width="400" height="400" alt="Screenshot 2025-12-22 at 22 42 56" src="https://github.com/user-attachments/assets/b11a8e96-13c7-477f-a8cf-12e893dc4b2a" />
<img width="400" height="400" alt="Screenshot 2025-12-22 at 22 41 51" src="https://github.com/user-attachments/assets/a4ab926a-e61d-4500-b551-873010d76ee0" />






## How to Run the Project

First, upload the Arduino code to the ESP32 drone controller and the ESP32-S3 camera module using the Arduino IDE. Ensure that the Wi-Fi credentials and UDP settings in the firmware match those configured on the laptop.

Next, set up the Python environment on the laptop by installing the required dependencies listed in the requirements files. Once the environment is ready, start the gesture recognition module to enable real-time hand gesture detection and command transmission.

After that, run the crowd detection module to receive the live video stream from the drone camera. The system will automatically perform person detection, count individuals in the frame, and generate a live crowd density heatmap.

When everything is running, the drone can be controlled entirely using hand gestures, while the ground station displays live aerial footage with crowd analytics.

---

## Conclusion

This project demonstrates the integration of intuitive human-computer interaction with intelligent aerial surveillance. By combining gesture recognition, embedded systems, and deep learning-based vision, the system offers a scalable and flexible approach to drone control and crowd monitoring. It serves as a practical example of how modern AI and IoT technologies can work together to solve real-world problems.
