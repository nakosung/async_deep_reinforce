# -*- coding: utf-8 -*-

LOCAL_T_MAX = 20 # repeat step size
RMSP_EPSILON = 1e-10 # epsilon parameter for RMSProp
CHECKPOINT_DIR = 'checkpoints'
LOG_FILE = 'tmp/a3c_log'
INITIAL_ALPHA_LOW = 1e-4    # log_uniform low limit for learning rate
INITIAL_ALPHA_HIGH = 1e-2   # log_uniform high limit for learning rate

PARALLEL_SIZE = 8 # parallel thread size
ROM = "pong.bin"     # action size = 3
#ROM = "breakout.bin" # action size = 4
ACTION_SIZE = 3 # action size

INITIAL_ALPHA_LOG_RATE = 0.4226 # log_uniform interpolate rate for learning rate (around 7 * 10^-4)
GAMMA = 0.99 # discount factor for rewards
ENTROPY_BETA = 0.1 # entropy regurarlization constant
MAX_TIME_STEP = 6 * 10**7
