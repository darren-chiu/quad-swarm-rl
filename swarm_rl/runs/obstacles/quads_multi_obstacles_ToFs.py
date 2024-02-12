from sample_factory.launcher.run_description import Experiment, ParamGrid, RunDescription
from swarm_rl.runs.obstacles.quad_obstacle_baseline import QUAD_BASELINE_CLI_8

_params = ParamGrid(
    [
        ("seed", [0000, 1111]),
        ("quads_num_agents", [1]),
        ("quads_obst_noise", [0.005, 0.01, 0.02, 0.03]),
    ]
)

OBSTACLE_MODEL_CLI = QUAD_BASELINE_CLI_8 + (
    ' --num_workers=36 --num_envs_per_worker=4 '
    '--quads_neighbor_visible_num=-1 --quads_neighbor_obs_type=none --quads_obstacle_obs_type=ToFs '
    '--with_wandb=True --wandb_project=Quad-Swarm-RL --wandb_user=multi-drones '
    '--wandb_group=ToFs-obst-noise'
)

_experiment = Experiment(
    "ToFs-obst-noise",
    OBSTACLE_MODEL_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription("ToFs-obst-noise", experiments=[_experiment])