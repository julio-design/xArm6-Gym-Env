from setuptools import setup
setup(name='gym_xarm6',
        author="Julio Ramirez",
        author_email="julio@jcrcx.xyz",
        description="xArm 6 robot environment for gym. It also contains a kinematic model of the robot.",
        url="https://github.com/ollintzinlab/xArm6-Gym-Env",
        version='0.0.2',
        licence="MIT",
        install_requires=[
            'gym[all]==0.15.3',
            "mujoco-py",
            "mujoco", # later this will become default
            "torch",
            "mpi4py",
            "pybullet",
            "tensorflow",
            'numpy']) # And any other dependencies required
