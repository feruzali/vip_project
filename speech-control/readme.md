# README for TurtleBot3 Voice Control

## Overview

This Python application provides a simple yet effective way to control a TurtleBot3 robot using voice commands. It leverages the power of speech recognition to convert spoken words into text and process them for robot control. The application features a graphical user interface (GUI) for real-time display of transcribed text and system messages.

## Features

- **Real-Time Speech Recognition**: Transcribes spoken words into text using Google's speech recognition service.
- **Graphical User Interface**: Displays transcribed text and status updates in real-time.
- **Continuous Listening**: The application listens continuously without the need to restart or trigger listening manually.
- **Error Handling**: Any issues during speech recognition are displayed in the GUI, making troubleshooting easier.

## Requirements

To run this application, you will need:

- Python 3.x
- `speech_recognition` library
- `PyAudio` library (for microphone input)
- `Tkinter` library (for the GUI)

## Installation

1. **Install Python**: Ensure that Python 3.x is installed on your system.
2. **Install Libraries**: Use pip to install necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**: Save the script as `turtlebot_voice_control.py` and run it using Python:
   ```bash
   python app.py
   ```

## Application Flow

- Upon launching, the application opens a GUI window titled "TurtleBot3 action through voice command".
- The application starts listening to the microphone input immediately.
- Spoken words are transcribed and displayed in the GUI window along with a 'Processing...' message.
- In case of any recognition errors or issues, an error message is displayed in the GUI.

## Note

This application is designed for controlling a TurtleBot3 robot.
