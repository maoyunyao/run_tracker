########################################################################
# YOU NEED TO IMPLEMENT THE FOLLOWING CODE SO THAT THIS TOOLKIT CAN HAVE 
# ACCESS TO YOUR TRACKER WITHOUT MOVING YOUR TRACKER TO THIS WORKSPACE
########################################################################
# Where your tracker is implemented:
tracker_path = '/data5/maoyy/Trackers'
import sys
sys.path.append(tracker_path)
from SiamFC import SiamFCTracker as TrackerClass

# Param(s) your tracker needed:
model_path = '/data5/maoyy/Trackers/SiamFC/models/siamfc_30.pth'
gpu_id = 0
params = [model_path, gpu_id]


##################################################
# YOU DO NOT NEED TO MODIFY THE FOLLOWING CODE
##################################################

# Methods to be integrated into your tracker class
from .method import track_dataset, track_sequence


def get_tracker():
    TrackerClass.track_dataset = track_dataset
    TrackerClass.track_sequence = track_sequence
    return TrackerClass(*params)


