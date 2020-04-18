########################################################################
# YOU NEED TO IMPLEMENT THE FOLLOWING CODE SO THAT THIS TOOLKIT CAN HAVE 
# ACCESS TO YOUR TRACKER WITHOUT MOVING YOUR TRACKER TO THIS WORKSPACE
########################################################################
# Where your tracker is implemented:
tracker_path = 'PATH TO YOUR TRACKER DIR'
import sys
sys.path.append(tracker_path)
from siamfc import "BEST_TRACKER" as TrackerClass

# Param(s) your tracker needed:
param1 = 'balabala'
param2 = 'bilibili'
params = [param1, param2]


##################################################
# YOU DO NOT NEED TO MODIFY THE FOLLOWING CODE
##################################################

# Methods to be integrated into your tracker class
from .method import track_dataset, track_sequence


def get_tracker():
    TrackerClass.track_dataset = track_dataset
    TrackerClass.track_sequence = track_sequence
    return TrackerClass(*params)


