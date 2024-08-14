from sample_factory.launcher.run_description import Experiment, ParamGrid, RunDescription
from swarm_rl.runs.obstacles.single_drone.quad_obstacle_single_baseline import QUAD_BASELINE_CLI_1

_params = ParamGrid(
    [
        ("seed", [3333]),
        ("quads_obstacle_tof_resolution", [8]),
        ("quads_obst_grid_size_random", [True]),
        ("normalize_input", [False]),
    ]
)

OBSTACLE_MODEL_CLI = QUAD_BASELINE_CLI_1 + (
    '--rnn_size=32 '
    ' --quads_obst_grid_size=0.5 --quads_obst_spawn_center=False --quads_obst_grid_size_range 0.5 0.8 '
    '--quads_mode=o_random_dynamic_goal --quads_obs_rel_rot=False --quads_dynamic_goal=True --quads_use_ctbr=True '
    '--quads_obst_hidden_size=16 --quads_obst_density=0.2 --quads_obstacle_obs_type=ToFs --quads_obst_noise=0.05 '
    '--with_wandb=True --wandb_project=Quad-Swarm-RL --wandb_user=darren-personal '
    '--wandb_group=sd_ctbr'
)

_experiment = Experiment(
    "dynamic_goal_discrete_curriculum",
    OBSTACLE_MODEL_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription("single_drone_multi_obst", experiments=[_experiment])