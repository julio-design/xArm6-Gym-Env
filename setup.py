from setuptools import setup
setup(name='gym_xarm6',
        author="Julio Ramirez",
        author_email="julio@jcrcx.xyz",
        description="xArm 6 robot environment for gym. It also contains a kinematic model of the robot.",
        url="https://github.com/ollintzinlab/xArm6-Gym-Env",
        version='0.0.1',
        licence="MIT",
        install_requires=[
            'gym[all]==0.15.3',
            "mujoco-py", "torch", "mpi4py",
            'numpy']) # And any other dependencies required
