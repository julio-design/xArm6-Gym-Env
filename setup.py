from setuptools import setup
setup(name='gym_xarm6',
        version='0.0.1',
        install_requires=['gym[all]==0.15.3',
            "mujoco-py",
            'numpy']) # And any other dependencies required
