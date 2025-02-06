# Real-Time-Object-Detection
## Overview
This project provides a simple real-time camera feedback application using OpenCV and Tkinter. The goal is to display live video from a webcam in a Tkinter window, allowing users to start and stop the video capture.

## Features
- Real-time camera feedback
- Start and stop video capture
- Easy to use and integrate

## Installation
1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/Real-Time-Object-Detection.git
  ```
2. Navigate to the project directory:
  ```bash
  cd Real-Time-Object-Detection
  ```
3. Install the required dependencies:
  ```bash
  pip install opencv-python-headless pillow
  ```

## Usage
1. Run the script:
  ```bash
  python camera_feedback.py
  ```
  A window titled "Camera feedback" will open, displaying the live video feed from your webcam.

  Use the "Start Capture" button to begin the video feed and the "Stop Capture" button to stop it.

## Code Overview
The main script `camera_feedback.py` uses OpenCV to capture video from the webcam and Tkinter to create a GUI for displaying the video feed. The video frames are converted from BGR to RGB format and then displayed in a Tkinter label.

### Key Functions
- `image_capture()`: Captures a frame from the webcam, converts it to RGB format, and updates the Tkinter label with the new frame.
- `start_capture()`: Starts the video capture process and disables the "Start Capture" button.
- `stop_capture()`: Stops the video capture process and enables the "Start Capture" button.
- `capture_frames()`: Continuously captures and displays frames as long as the capturing flag is set to True.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.