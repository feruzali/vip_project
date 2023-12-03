import rospy
from geometry_msgs.msg import Twist
import threading
import speech_recognition as sr

# Initialize the recognizer for speech recognition
r = sr.Recognizer()

# Function to handle TurtleBot3 movement based on voice command
def handle_movement(command):
    """
    Converts a voice command into TurtleBot3 movement.

    Parameters:
    command (str): The voice command as transcribed text.

    The function publishes Twist messages to the '/cmd_vel' topic
    to control the TurtleBot3's linear and angular velocities.
    """
    # ROS publisher to send Twist messages to TurtleBot3
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtlebot3_voice_control', anonymous=True)
    rate = rospy.Rate(10)  # Frequency of 10 Hz

    move_cmd = Twist()

    # Translate voice commands to movement commands
    if command == "move forward":
        move_cmd.linear.x = 0.5  # Positive linear velocity
        move_cmd.angular.z = 0.0
    elif command == "move backward":
        move_cmd.linear.x = -0.5  # Negative linear velocity
        move_cmd.angular.z = 0.0
    elif command == "turn left":
        move_cmd.angular.z = 1.0  # Positive angular velocity
    elif command == "turn right":
        move_cmd.angular.z = -1.0  # Negative angular velocity
    else:
        print("Unknown command")

    # Execute the movement command
    for i in range(5):
        pub.publish(move_cmd)
        rate.sleep()

    # Stop the robot
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

# Function to listen, transcribe speech, and act on it
def listen_and_act():
    """
    Listens to speech input and transcribes it to text.
    Calls the handle_movement function with the transcribed text.
    """
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            # Transcribe speech to text
            text = r.recognize_google(audio)
            print("You said: " + text)
            # Call movement handler with the transcribed text
            handle_movement(text.lower())
        except Exception as e:
            print("Error: " + str(e))

# Main loop for continuous listening and acting
def start_listening():
    """
    Starts the continuous listening loop.
    This function runs until the ROS node is shut down.
    """
    while not rospy.is_shutdown():
        listen_and_act()

# Run the listening function in a separate thread
threading.Thread(target=start_listening).start()
