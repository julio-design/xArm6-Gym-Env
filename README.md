# xArm6 inverse kinematics with DDPG+HER
Creation of a new environment in OpenAI gym for the xArm6 robot from UFactory. The model uses [Deep Deterministic Policy Gradient](https://arxiv.org/abs/1509.02971) (DDPG) for continious actions and [Hindsight Experience Replay](https://arxiv.org/abs/1707.01495) (HER).

## Installation
Follow this instructions to be able to use the xArm6 enviroment for OpenAI gym. You can use your own policies to train the model, but here we will use DDPG + HER.

Before the installation, we need to get [MuJoCo](https://mujoco.org) (multi-joint dynamics in contact) physics simulator.

> **Note:** For easier installation we recomend using Unix based OS.

1. Download MuJoCo
    + [Windows](https://roboti.us/download/mujoco200_win64.zip)
    + [Linux](https://roboti.us/download/mujoco200_linux.zip)
    + [MacOS](https://roboti.us/download/mujoco200_macos.zip)
2. Create a folder in your home directory named `.mujoco` and unzip the file here.
3. Download the [activation key licence](https://roboti.us/file/mjkey.txt) and put it inside `.mujoco/mujoco200/`.
4. Modify the `.bashrc` and add the following lines:

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/julio/.mujoco/mujoco200/bin
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

Once you have it, run `pip install -e .` to install the environment.
