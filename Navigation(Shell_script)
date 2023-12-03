#!/bin/bash

# Set TurtleBot3 model
export TURTLEBOT3_MODEL=burger

# Launch TurtleBot3 Bringup
ros2 launch turtlebot3_bringup robot.launch.py &

# Wait for the TurtleBot3 Bringup to start
sleep 5

# Launch TurtleBot3 Navigation2 with a specified map
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/map.yaml &

# Wait for the TurtleBot3 Navigation2 to start
sleep 5

# Launch TurtleBot3 teleoperation
ros2 run turtlebot3_teleop teleop_keyboard

# When teleoperation ends, terminate the launched nodes
pkill -f 'ros2 launch turtlebot3_bringup'
pkill -f 'ros2 launch turtlebot3_navigation2'

chmod +x navigate_turtlebot.sh

./navigate_turtlebot.sh

# 
Certainly! To create a shell script for TurtleBot3 navigation, you can follow the steps below. Create a new file, let's say navigate_turtlebot.sh, and add the following content:

bash
Copy code
#!/bin/bash

# Set TurtleBot3 model
export TURTLEBOT3_MODEL=burger

# Launch TurtleBot3 Bringup
ros2 launch turtlebot3_bringup robot.launch.py &

# Wait for the TurtleBot3 Bringup to start
sleep 5

# Launch TurtleBot3 Navigation2 with a specified map
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/map.yaml &

# Wait for the TurtleBot3 Navigation2 to start
sleep 5

# Launch TurtleBot3 teleoperation
ros2 run turtlebot3_teleop teleop_keyboard

# When teleoperation ends, terminate the launched nodes
pkill -f 'ros2 launch turtlebot3_bringup'
pkill -f 'ros2 launch turtlebot3_navigation2'
Make the script executable:

bash
Copy code
chmod +x navigate_turtlebot.sh
You can then run the script by executing:

bash
Copy code
./navigate_turtlebot.sh
This script does the following:

Sets the TurtleBot3 model to "burger."
Launches TurtleBot3 Bringup in the background.
Waits for 5 seconds to allow Bringup to start.
Launches TurtleBot3 Navigation2 with a specified map in the background.
Waits for 5 seconds to allow Navigation2 to start.
Launches TurtleBot3 teleoperation.
When teleoperation ends, it terminates the launched nodes.
Make sure to replace $HOME/map.yaml with the actual path to your map file. Adjust the sleep durations based on your system's performance and startup times.

Please note that this script assumes that the TurtleBot3 Bringup and Navigation2 can run concurrently. If you face issues or if the sequence needs adjustment, you might need to experiment with the sleep durations and the order of launching nodes.