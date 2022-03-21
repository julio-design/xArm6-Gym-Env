import os
from gym import utils
from gym_xarm6.envs import xarm6_env


# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('assets', 'reach.xml')

class xArm6ReachEnv(xarm6_env.xArm6Env, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': -0.3,
            'robot0:slide1': -0.,
            'robot0:slide2': 0.,
        }
        xarm6_env.xArm6Env.__init__(
            self, MODEL_XML_PATH, has_object=False, block_gripper=False, n_substeps=20,
            gripper_extra_height=0., target_in_the_air=False, target_offset=0.0,
            obj_range=0.25, target_range=0.25, distance_threshold=0.003,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)
