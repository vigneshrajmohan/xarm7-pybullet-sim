from pynput import keyboard
import pybullet as p
import time
import pybullet_data
import os

# Define a flag variable
exit_simulation = False

# Define the key press callback function
def on_press(key):
    global exit_simulation
    try:
        if key.char == 'q':
            exit_simulation = True
    except AttributeError:
        pass

# Start listening for key presses
listener = keyboard.Listener(on_press=on_press)
listener.start()

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")

# Assume URDF files are in the same directory
urdf_path = 'xarm7_with_gripper.urdf'
urdf_dir = os.path.dirname(urdf_path)
p.setAdditionalSearchPath(urdf_dir)

startPos_arm = [0,0,0]
startOrientation_arm = p.getQuaternionFromEuler([0,0,0])
armId = p.loadURDF(urdf_path, startPos_arm, startOrientation_arm)

# Load table
startPos_table = [1,0,0]  # adjust position as needed
tableId = p.loadURDF("table.urdf", startPos_table)

# Load pan
startPos_pan = [1,0.5,1]  # adjust position as needed
panId = p.loadURDF("pan.urdf", startPos_pan)

# Load spatula
startPos_spatula = [1,-0.5,1]  # adjust position as needed
spatulaId = p.loadURDF("spatula.urdf", startPos_spatula)

while not exit_simulation:
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
listener.stop()
