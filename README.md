# Zipper
Zipper is a little robot buddy that tracks the face of a user using facial  recognition and moves according to the position of the face 

This project animates a pair of digital eyes on an OLED display and moves servos based on Serial input. The eyes blink periodically and can be controlled with external commands.

## Features  
- OLED display shows animated eyes (open, close, blink).  
- Servos move based on serial input (`X, Y` angles).  
- Eyes automatically blink every 4 seconds.  
- Wake-up animation when powered on.  

## Hardware Requirements  
- Arduino (Uno, Mega, or compatible)  
- SSD1306 OLED Display (128x64)  
- 2x Servo Motors  
- Jumper wires  

## Setup & Installation  
1. Install the required libraries:  
   - [Adafruit SSD1306](https://github.com/adafruit/Adafruit_SSD1306)  
   - [Adafruit GFX](https://github.com/adafruit/Adafruit-GFX-Library)  
   - [Servo](https://www.arduino.cc/en/reference/servo)  

2. Connect components as follows:  
   - **OLED Display:** SDA → A4, SCL → A5 (on Arduino Uno)  
   - **Servo X:** Pin 9  
   - **Servo Y:** Pin 10  
   - **Power:** Servos to 5V/GND  

3. Upload the `eyes.ino` sketch to your Arduino.  

## Usage  
- The program automatically blinks the eyes.  
- Send Serial commands (`90, 90`) to adjust servo positions.  
- Default positions: **90° X-axis**, **90° Y-axis**.  

## License  
This project is open-source under the MIT License.  
