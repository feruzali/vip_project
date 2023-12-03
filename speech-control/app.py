import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext, font
import threading

# Initialize the recognizer
# This is used for recognizing speech
r = sr.Recognizer()

# Initialize Tkinter for GUI
root = tk.Tk()
root.title("TurtleBot3 action through voice command")

# Custom Font for text widget
custom_font = font.Font(family="Helvetica", size=12)

# ScrolledText Widget
# This widget will display the transcribed text
text_widget = scrolledtext.ScrolledText(root, height=10, width=50, font=custom_font)
text_widget.pack(padx=10, pady=10)

def update_text(text):
    """
    Function to update the text widget.
    It inserts the given text to the text widget and scrolls to the end.

    :param text: Text to be added to the widget.
    """
    text_widget.insert(tk.END, text + '\nProcessing...\n')
    text_widget.see(tk.END)

def listen_and_transcribe():
    """
    Function to listen to audio from the microphone and transcribe it.
    It listens to the audio, transcribes it using Google's speech recognition,
    and updates the GUI with the transcribed text.
    """
    with sr.Microphone() as source:
        # Adjusts for ambient noise to reduce errors
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            update_text("Listening ...: " + text)
        except Exception as e:
            # If an error occurs, it is displayed in the GUI
            update_text("Error: " + str(e))

def start_listening():
    """
    Function to start the listening process in a continuous loop.
    It repeatedly calls listen_and_transcribe function to continuously
    listen and process audio.
    """
    while True:
        listen_and_transcribe()

# Start listening in a separate thread
# This prevents blocking the main thread and keeps the GUI responsive
threading.Thread(target=start_listening).start()

# Start the Tkinter event loop
# This call is blocking and will display the GUI
root.mainloop()
