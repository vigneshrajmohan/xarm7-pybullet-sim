import pybullet as p
import time
import pybullet_data
import os

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])

# Add the directory containing the missing file to the URDF search path
# p.setAdditionalSearchPath('/home/vignesh/Documents/Research/Spring2023/sim_test/meshes')
urdf_path = 'xarm7_with_gripper.urdf'
urdf_dir = os.path.dirname(urdf_path)
p.setAdditionalSearchPath(urdf_dir)

boxId = p.loadURDF(urdf_path, startPos, startOrientation)

#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
