# Photos
#### Final build photos
![SIDE](https://github.com/user-attachments/assets/57c5469c-304b-44fb-ae81-99ee07c73956)
![FRONT](https://github.com/user-attachments/assets/d413f298-5c2f-487b-84e0-738abfed6690)
![TOP](https://github.com/user-attachments/assets/838fdc28-0eb5-4132-94af-fb1f389bd87d)


#### Old Broken Setup
![IMG_1874](https://github.com/user-attachments/assets/b4212e08-dfdb-458d-bff0-1aa0173c48ae)

#### Driver code
<img width="1920" height="1080" alt="driver" src="https://github.com/user-attachments/assets/edabe69b-d4ce-4d7b-a77d-1e3819e48efb" />

# Mona Personal Security
A self-honing turret which uses a camera and OpenCV in order to detect faces and autonomously move the turret to shoot projectiles at them.
The name, is of course, an ode to Mona, who accompanied us for many hours in GitHub HQ.

# Software
There are two parts to the software, the driver code that runs the camera from your laptop, and the firmware in the Raspberry Pico that recieves instructions and moves the motors.
The driver code needs to be launched after the firmware has been flashed, and the device connected via USB. Change the serial_port variable used in driver.py accordingly. Run the code, and tinker with camera_index until it works. (Usually, 0 or 1). The firmware should be flashed with Arduino IDE, we tested with version 2.3.6

# CAD
In CAD, we created the top of the main structure, the bottom, and the middle as individual components. We also created the piece to go on the railing and hold the motors for shooting. There was also a mount we created that hooks into the top of the main structure. This is where we bolted in the webcam.


# Challenges
We struggled with getting the stepper motor to work, but after many hours, and some outside help, we realized that the board, a XIAO RP2040 was fried, and we switched to a Raspberry Pi Pico. This was our biggest problem, the stepper motor held us back several times.


