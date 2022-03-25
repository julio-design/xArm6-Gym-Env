from gym.envs.registration import registry, register, make, spec

def _merge(a, b):
    a.update(b);
    return a;

for reward_type in ['sparse', 'dense']:
    suffix = 'Dense' if reward_type == 'dense' else ''
    kwargs = {
        'reward_type': reward_type,
    }

    register(
        id='xArm6Reach{}-v0'.format(suffix),
        entry_point='gym_xarm6.envs:xArm6ReachEnv',
        kwargs=kwargs,
        max_episode_steps=100,
    )
