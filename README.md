# xArm6 inverse kinematics with DDPG+HER
Creation of a new environment in OpenAI gym for the xArm6 robot from UFactory. The model uses [Deep Deterministic Policy Gradient](https://arxiv.org/abs/1509.02971) (DDPG) for continious actions and [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495) (HER).

### Author
Julio Cesar RAMIREZ CEBALLOS

## Usage and installation
Follow this instructions to be able to use the xArm6 enviroment for OpenAI gym. You can use your own policies to train the model, but here we will use DDPG + HER.

Before the installation, we need to get [MuJoCo](https://mujoco.org) (multi-joint dynamics in contact) physics simulator.

1. Download MuJoCo
    + [Windows](https://github.com/deepmind/mujoco/releases/download/2.1.1/mujoco-2.1.1-windows-x86_64.zip)
    + [Linux](https://github.com/deepmind/mujoco/releases/download/2.1.1/mujoco-2.1.1-linux-aarch64.tar.gz)
    + [MacOS](https://github.com/deepmind/mujoco/releases/download/2.1.1/mujoco-2.1.1-macos-universal2.dmg)
    + [Source](https://github.com/deepmind/mujoco/archive/refs/tags/2.1.1.zip)
2. Create a folder in your home directory named `.mujoco` and unzip the file here.
3. kjl
