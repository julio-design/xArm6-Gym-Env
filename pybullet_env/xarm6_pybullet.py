import numpy as np
import pybullet as p
import pybullet_data
import time

"""
class xArmEnv():
    def __init__(self):
        self.state = self.init_state()
        self.step_count = 0

    def init_state(self):
        p.connect(p.GUI)
        p.resetSimulation()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robotid = p.loadURDF("xarm/xarm6_robot.urdf", [0, 0, 0,], [0, 0, 0, 1], useFixedBase = True)
        p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
        self.focus_position, _ = p.getBasePositionAndOrientation(self.robotid)
        p.resetDebugVisualizerCamera(cameraDistance=3, cameraYaw=0, cameraPitch=-40, cameraTargetPosition = self.focus_position)
        tool_pos = p.getLinkState(self.robotid, 6) [:2]
        obs = np.array([tool_pos]).flatten()
        return obs

    def reset(self):
        p.disconnect()
        self.state = self.init_state()
        self.step_count = 0

    def step(self, action):
        self.step_count += 1
        p.setJointMotorControlArray(self.robotid, [1, 2, 3, 4, 5, 6], p.POSITION_CONTROL, [action])
        p.stepSimulation()
        tool_pos = p.getLinkState(self.robotid, 6)[:2]

        if (self.step_count >= 50):
            self.reset()
            tool_pos = p.getLinkState(self.robotid, 6)[:2]
            obs = np.array([tool_pos]).flatten()
            self.state = obs
            reward = -1
            done = True
            return reward, done

        obs = np.array([tool_pos]).flatten()
        self.state = obs
        done = False
        reward = -1
        return reward, done
"""

p.connect(p.GUI)
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
targid= p.loadURDF("xarm/xarm6_robot.urdf", [0, 0, 0,], [0, 0, 0, 1], useFixedBase = True)
p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
focus_position, _ = p.getBasePositionAndOrientation(targid)
p.setRealTimeSimulation(0)
p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
obj_of_focus = targid

jointid = np.array([1, 2, 3, 4, 5, 6])
jtype, jlower, jupper, action = [], [], [], []

for i in range(len(jointid)):
    jtype.append(p.getJointInfo(targid, jointid[i])[2])
    jlower.append(p.getJointInfo(targid, jointid[i])[8])
    jupper.append(p.getJointInfo(targid, jointid[i])[9])

for step in range(1000):
    #joint_1_targ = np.random.uniform(jlower[0], jupper[0])
    #joint_2_targ = np.random.uniform(jlower[1], jupper[1])
    #joint_3_targ = np.random.uniform(jlower[2], jupper[2])
    #joint_4_targ = np.random.uniform(jlower[3], jupper[3])
    #joint_5_targ = np.random.uniform(jlower[4], jupper[4])
    #joint_6_targ = np.random.uniform(jlower[5], jupper[5])
    for i in range(len(jointid)):
        action.append(np.random.uniform(jlower[i], jupper[i]))
    #p.setJointMotorControlArray(targid, [1, 2, 3, 4, 5, 6], p.POSITION_CONTROL, targetPositions = [joint_1_targ, joint_2_targ, joint_3_targ, joint_4_targ, joint_5_targ, joint_6_targ])
    p.setJointMotorControlArray(targid, [1, 2, 3, 4, 5, 6], p.POSITION_CONTROL, targetPositions = np.array(action))
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    p.resetDebugVisualizerCamera(cameraDistance=3, cameraYaw=0, cameraPitch=-40, cameraTargetPosition = focus_position)
    p.stepSimulation()
    time.sleep(.01)
