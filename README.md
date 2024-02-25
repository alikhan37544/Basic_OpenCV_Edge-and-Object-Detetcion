# Motion Detection System

A Python-based motion detection system that leverages OpenCV for real-time surveillance and security purposes. This application processes video from a webcam to detect motion, highlighting movement within the video feed. It's designed to be a starting point for anyone interested in developing their own motion detection features for projects like home security systems, wildlife monitoring, or any scenario requiring motion detection.

## Getting Started

### Prerequisites

Before you begin, you'll need to have the following installed on your system:
- Python 3.x
- OpenCV
- NumPy

You can install the required libraries using pip:

```
pip install opencv-python numpy
```

### Installation

Clone this repository to your local machine to get started:

```
https://github.com/alikhan37544/Basic_OpenCV_Edge-and-Object-Detetcion.git
```

Navigate to the cloned directory:

```
cd motion-detection-system
```

### Running the Application

To start the motion detection, simply execute the script with Python:

```
python motion_detection.py
```

## How It Works

The application captures video frames from the webcam, processes them to detect motion, and displays the output in real-time. Key steps include:
- Converting video frames to grayscale and applying Gaussian Blur to reduce noise.
- Calculating the absolute difference between the current frame and the previous frame to detect changes.
- Applying a binary threshold to highlight significant changes.
- Dilating the thresholded image to enhance detected features.
- Identifying and highlighting contours of detected motion in the live video feed.

## Features

- **Real-Time Motion Detection**: Monitors and detects movement in the video captured by the webcam.
- **Visual Feedback**: Highlights detected motion with rectangles in the live video feed.
- **Adjustable Detection Parameters**: Allows for customization of detection sensitivity and other parameters.

## Future Prospects

- **Sensitivity Adjustment**: Dynamic adjustment of the detection sensitivity to adapt to different environments and requirements.
- **Alert System**: Integration of email or SMS notifications when motion is detected.
- **Recording**: Option to automatically start recording video upon detection of motion.
- **Object Recognition**: Incorporation of object recognition to identify and differentiate between types of motion.
- **Remote Monitoring**: Development of a web interface for live streaming and remote control of the motion detection system.
- **Cloud Integration**: Cloud storage for recorded footage, ensuring data is safe and accessible from anywhere.

## Troubleshooting

- **No Video Feed**: If the application fails to open the video feed, ensure your webcam is properly connected and not in use by another application. You may need to adjust the `cv2.VideoCapture` index to match your webcam's configuration.
- **Performance Issues**: If you experience lag or stuttering in the video feed, try reducing the resolution or frame rate of the video capture.
- **Dependency Problems**: Ensure that you have installed the correct versions of Python, OpenCV, and NumPy. Incompatibilities may cause unexpected issues.

## Contributing

Contributions to improve the motion detection system are welcome. Whether it's adding new features, improving existing ones, or fixing bugs, your input is valuable. Please feel free to fork the repository, make changes, and submit a pull request.
