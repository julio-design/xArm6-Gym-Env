# xArm6 inverse kinematics with DDPG+HER
`gym-xarm6` is a gym environment for path planning with xArm6 robot using openai gym framework. The environment
Creation of a new environment in OpenAI gym for the xArm6 robot from UFactory. The model uses [Deep Deterministic Policy Gradient](https://arxiv.org/abs/1509.02971) (DDPG) for continious actions and [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495) (HER).

## Installation

### Requirements

+ python3.6+ environment by one of the following:
    + conda
    + virtualenv
    + venv
    + system python
+ swig
+ libosmesa6-dev
+ patchelf
+ libopenmpi-dev
+ mpi4py (install it with pip or conda)
+ openai [baselines](https://github.com/openai/baselines/tree/90d66776a49ad5e732b935dfc891bfbd06035ed2)

Follow this instructions to be able to use the xArm6 enviroment for OpenAI gym. You can use your own policies to train the model, but here we will use DDPG + HER.

Before the installation, we need to get [MuJoCo](https://mujoco.org) (multi-joint dynamics in contact) physics simulator.

> **Note:** For easier installation we recomend using Unix based OS.
> 1. The code was tested on Ubuntu 20.04, Debian 11 succesfully.
> 2. Have fun manipulating the code and the model!

1. Download MuJoCo
    + [Windows](https://roboti.us/download/mujoco200_win64.zip)
    + [Linux](https://roboti.us/download/mujoco200_linux.zip)
    + [MacOS](https://roboti.us/download/mujoco200_macos.zip)
2. Create a folder in your home directory named `.mujoco` and unzip the file here.
3. Download the [activation key licence](https://roboti.us/file/mjkey.txt) and put it inside `.mujoco/mujoco200/` and `.mujoco/mujoco200/bin/`.
4. Modify the `.bashrc` and add the following lines:

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/your/home/dir/.mujoco/mujoco200/bin
```

5. Test that MuJoCo is working properly.

```
cd ~/.mujoco/mujoco200/bin
./simulate ../models/humanoid.xml
```

Now clone this repository.

```
git clone https://github.com/ollintzinlab/xArm6-Gym-Env.git
```

Once you have it, `cd` into the cloned directory an run `pip install -e .` to install the environment.
<!-- sudo apt-get install libosmesa6-dev -->

### Test
Train the model by running:

```
python her/train.py --env-name="xArm6Reach-v0" | tee her/reach.log
```

Test the model by running:

```
python her/demo.py --env-name="xArm6Reach-v0"
```

## Usage

In `gym_xarm6/envs/reach.py` you can modify the position of the robot in the world frame.

```
...
        initial_qpos = {
            'robot0:slide0': 0.,
            'robot0:slide1': 0.,
            'robot0:slide2': 0.,
        }
...
```

The variable `distance_threshold` allows you to change de precision of the robot. It is used to calculate the normal distance from the **tool frame** of the robot to the target position in a cartesian frame.
