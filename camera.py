**Hardware Requirements:**

* Raspberry Pi Model A/B/B+
* Pi Camera
* Buzzer
* 2 Push Buttons
* LED
* Breadboard
* Jumper Wires
* Power Supply
* Ethernet Cable / Wi-Fi
* Monitor, Keyboard, Mouse (Optional, for without headless connection) [cite: 111, 110]

**Software Requirements:**

* Raspbian Stretch OS
* Python Script [cite: 111, 110]

**Steps:**

1. **Connect the Pi Camera:** Connect the Pi Camera to the Raspberry Pi's camera port (blue side of the cable facing the Ethernet connection). [cite: 117, 118, 119]

2. **Enable the Pi Camera:**
   * Open a terminal window.
   * Type the command `sudo raspi-config` and press Enter.
   * Select "Interfacing Options," then "Camera," and then "Enable."
   * Reboot the Raspberry Pi using the command `sudo reboot`. [cite: 120, 121]

3. **Create a Folder for Images:**
   * After rebooting, create a folder to store the captured images. For example, you can create a folder named "Visitors" on the desktop: `/home/pi/Desktop/Visitors`. [cite: 122, 123]

4. **Install Pi-Camera Packages:**
   * Run the following commands in the terminal to install the necessary packages:
     ```bash
     sudo apt-get install python-picamera
     sudo apt-get install python3-picamera
     sudo pip install picamera
     ``` [cite: 124, 125]

5. **Write the Python Script:**
   * Open a text editor (like IDLE) and paste the following Python code:
     ```python
     import time
     import picamera

     camera = picamera.PiCamera()
     camera.resolution = (1024, 768)
     camera.start_preview()
     time.sleep(2)
     camera.capture('test.jpg')
     camera.stop_preview()
     ``` [cite: 124, 125]

6. **Save and Run the Script:**
   * Save the code as a Python file (e.g., "capture_image.py").
   * Open a terminal window and navigate to the directory where you saved the file.
   * Run the script using the command `python3 capture_image.py`. [cite: 124, 125]

**Explanation:**

* The script initializes the Pi Camera and sets the resolution to 1024x768 pixels.
* It starts the camera preview, waits for 2 seconds, and then captures an image named "test.jpg."
* The captured image will be saved in the same directory where the script is located. You can change the filename and path in the `camera.capture()` function. [cite: 124, 125]

**Additional Notes:**

* The camera preview only works when a monitor is connected to the Raspberry Pi. Remote access methods like SSH or VNC will not display the preview. [cite: 119]
* You can modify the script to capture images based on certain events, such as a button press or motion detection, by adding appropriate input mechanisms and logic.
* For more advanced camera functionalities, refer to the official Raspberry Pi Camera documentation.
