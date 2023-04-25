def crazyflie_params(extra_deck):
    ## See: Ref[2] for details
    ## Geometric parameters for Inertia and the model
    geom_params = {}
    geom_params["body"] = {"l": 0.03, "w": 0.03, "h": 0.004, "m": 0.005}
    if extra_deck == 0:
        # Battery: 9e-3; four markers: 0.2e-3 * 4 = 0.8e-3; + Some surplus
        geom_params["payload"] = {"l": 0.035, "w": 0.02, "h": 0.008, "m": 0.01}
    elif extra_deck == 1:
        # Based on extra_deck = 0
        # marker deck: 1.6e-3; LED-ring deck: 3.3e-3;
        # assume we have some extra weight that we didn't consider, such as glue = 0.3e-3
        # Total = 9e-3 + 0.8e-3 + 1.6e-3 + 3.3e-3 + 0.3e-3 = 1.47e-2 + 0.3e-3 = 1.5e-2
        geom_params["payload"] = {"l": 0.035, "w": 0.02, "h": 0.008, "m": 0.015}
    elif extra_deck == 2:
        # Based on extra_deck = 1
        # AI deck: 4.4e-3;
        # Total: 15 e-3 + 4.4 e-3 = 19.4e-3 = 1.94e-2
        geom_params["payload"] = {"l": 0.035, "w": 0.02, "h": 0.008, "m": 0.0194}
    geom_params["arms"] = {"l": 0.022, "w":0.005, "h":0.005, "m":0.001}
    geom_params["motors"] = {"h":0.02, "r":0.0035, "m":0.0015}
    geom_params["propellers"] = {"h":0.002, "r":0.022, "m":0.00075}
    
    geom_params["motor_pos"] = {"xyz": [0.065/2, 0.065/2, 0.]}
    geom_params["arms_pos"] = {"angle": 45., "z": 0.}
    geom_params["payload_pos"] = {"xy": [0., 0.], "z_sign": 1}
    # z_sing corresponds to location (+1 - on top of the body, -1 - on the bottom of the body)

    ## Damping parameters
    # damp_params = {"vel": 0.001, "omega_quadratic": 0.015}
    damp_params = {"vel": 0.0, "omega_quadratic": 0.0}

    ## Noise parameters
    noise_params = {}
    noise_params["thrust_noise_ratio"] = 0.05

    ## Motor parameters
    motor_params = {"thrust_to_weight" : 1.9, #2.18
                    "assymetry": [1.0, 1.0, 1.0, 1.0],
                    "torque_to_thrust": 0.006, #0.005964552
                    "linearity": 1.0, #0.424 for CrazyFlie w/o correction in firmware (See [2])
                    "C_drag": 0.000, # 3052 * 9.1785e-07  #3052 * 8.06428e-05, # 0.246
                    "C_roll": 0.000, #3052 * 0.000001 # 0.0003
                    "damp_time_up": 0.15, #0.15, #0.15 - See: [4] for details on motor damping. Note: these are rotational velocity damp params.
                    "damp_time_down": 0.15 #2.0, #2.0
                    }

    ## Summarizing
    params = {
        "geom": geom_params, 
        "damp": damp_params, 
        "noise": noise_params,
        "motor": motor_params
    }
    return params


def defaultquad_params():
    # Similar to AscTec Hummingbird: Ref[3]
    ## Geometric parameters for Inertia and the model
    geom_params = {}
    geom_params["body"] = {"l": 0.1, "w": 0.1, "h": 0.085, "m": 0.5}
    geom_params["payload"] = {"l": 0.12, "w": 0.12, "h": 0.04, "m": 0.1}
    geom_params["arms"] = {"l": 0.1, "w":0.015, "h":0.015, "m":0.025} #0.17 total arm
    geom_params["motors"] = {"h":0.02, "r":0.025, "m":0.02}
    geom_params["propellers"] = {"h":0.001, "r":0.1, "m":0.009}
    
    geom_params["motor_pos"] = {"xyz": [0.12, 0.12, 0.]}
    geom_params["arms_pos"] = {"angle": 45., "z": 0.}
    geom_params["payload_pos"] = {"xy": [0., 0.], "z_sign": -1}
    # z_sing corresponds to location (+1 - on top of the body, -1 - on the bottom of the body)
    
    ## Damping parameters
    # damp_params = {"vel": 0.001, "omega_quadratic": 0.015}
    damp_params = {"vel": 0.0, "omega_quadratic": 0.0}

    ## Noise parameters
    noise_params = {}
    noise_params["thrust_noise_ratio"] = 0.05
    
    ## Motor parameters
    motor_params = {"thrust_to_weight" : 2.8,
                    "assymetry": [1.0, 1.0, 1.0, 1.0], 
                    "torque_to_thrust": 0.05,
                    "linearity": 1.0, # 0.0476 for Hummingbird (See [5]) if we want to use RPMs instead of force.
                    "C_drag": 0.,
                    "C_roll": 0.,
                    "damp_time_up": 0,
                    "damp_time_down": 0
                    }
    ## Summarizing
    params = {
        "geom": geom_params, 
        "damp": damp_params, 
        "noise": noise_params,
        "motor": motor_params
    }
    return params


def mediumquad_params():
    # Similar to AscTec Hummingbird: Ref[3]
    ## Geometric parameters for Inertia and the model
    geom_params = {}
    geom_params["body"] = {"l": 0.04, "w": 0.04, "h": 0.04, "m": 0.04}
    geom_params["payload"] = {"l": 0.06, "w": 0.015, "h": 0.015, "m": 0.029}
    geom_params["arms"] = {"l": 0.04, "w":0.01, "h":0.003, "m":0.006} #0.17 total arm
    geom_params["motors"] = {"h":0.013, "r":0.007, "m":0.006}
    geom_params["propellers"] = {"h":0.007, "r":0.035, "m":0.0012}
    
    geom_params["motor_pos"] = {"xyz": [0.046, 0.046, 0.]}##############
    geom_params["arms_pos"] = {"angle": 45., "z": 0.}
    geom_params["payload_pos"] = {"xy": [0., 0.], "z_sign": -1}
    # z_sing corresponds to location (+1 - on top of the body, -1 - on the bottom of the body)
    
    ## Damping parameters
    # damp_params = {"vel": 0.001, "omega_quadratic": 0.015}
    damp_params = {"vel": 0.0, "omega_quadratic": 0.0}

    ## Noise parameters
    noise_params = {}
    noise_params["thrust_noise_ratio"] = 0.05
    
    ## Motor parameters
    motor_params = {"thrust_to_weight" : 2.5,
                    "assymetry": [1.0, 1.0, 1.0, 1.0], 
                    "torque_to_thrust": 0.05,
                    "linearity": 1.0, # 0.0476 for Hummingbird (See [5]) if we want to use RPMs instead of force.
                    "C_drag": 0.,
                    "C_roll": 0.,
                    "damp_time_up": 0.15,
                    "damp_time_down": 0.15
                    }
    ## Summarizing
    params = {
        "geom": geom_params, 
        "damp": damp_params, 
        "noise": noise_params,
        "motor": motor_params
    }
    return params


def crazyflie_lowinertia_params():
    ## See: Ref[2] for details
    ## Geometric parameters for Inertia and the model
    geom_params = {}
    geom_params["body"] = {"l": 0.03, "w": 0.03, "h": 0.004, "m": 0.014}
    geom_params["payload"] = {"l": 0.035, "w": 0.02, "h": 0.008, "m": 0.01}
    geom_params["arms"] = {"l": 0.022, "w":0.005, "h":0.005, "m":0.0005}
    geom_params["motors"] = {"h":0.02, "r":0.0035, "m":0.0005}
    geom_params["propellers"] = {"h":0.002, "r":0.022, "m":0.0000075}
    
    geom_params["motor_pos"] = {"xyz": [0.065/2, 0.065/2, 0.]}
    geom_params["arms_pos"] = {"angle": 45., "z": 0.}
    geom_params["payload_pos"] = {"xy": [0., 0.], "z_sign": 1}
    # z_sing corresponds to location (+1 - on top of the body, -1 - on the bottom of the body)

    ## Damping parameters
    # damp_params = {"vel": 0.001, "omega_quadratic": 0.015}
    damp_params = {"vel": 0.0, "omega_quadratic": 0.0}

    ## Noise parameters
    noise_params = {}
    noise_params["thrust_noise_ratio"] = 0.05

    ## Motor parameters
    motor_params = {"thrust_to_weight" : 1.9, #2.18
                    "assymetry": [1.0, 1.0, 1.0, 1.0],
                    "torque_to_thrust": 0.006, #0.005964552
                    "linearity": 1.0, #0.424 for CrazyFlie w/o correction in firmware (See [2])
                    "C_drag": 0.000, # 3052 * 9.1785e-07  #3052 * 8.06428e-05, # 0.246
                    "C_roll": 0.000, #3052 * 0.000001 # 0.0003
                    "damp_time_up": 0.15, #0.15, #0.15 - See: [4] for details on motor damping. Note: these are rotational velocity damp params.
                    "damp_time_down": 0.15 #2.0, #2.0
                    }

    ## Summarizing
    params = {
        "geom": geom_params, 
        "damp": damp_params, 
        "noise": noise_params,
        "motor": motor_params
    }
    # print(params)
    return params