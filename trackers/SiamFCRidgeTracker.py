########################################################################
# YOU NEED TO IMPLEMENT THE FOLLOWING CODE SO THAT THIS TOOLKIT CAN HAVE 
# ACCESS TO YOUR TRACKER WITHOUT MOVING YOUR TRACKER TO THIS WORKSPACE
########################################################################
# Where your tracker is implemented:
tracker_path = '/data5/maoyy/SiamFC_ridge_train'
import sys
sys.path.append(tracker_path)
from siamfc import SiamFCRidgeTracker as TrackerClass

# Param(s) your tracker needed:
model_path = '/data5/maoyy/SiamFC_ridge_train/models/siamfc_ridge_80.pth'
params = [model_path]


##################################################
# YOU DO NOT NEED TO MODIFY THE FOLLOWING CODE
##################################################

# Methods to be integrated into your tracker class
from .method import track_dataset, track_sequence


def get_tracker():
    TrackerClass.track_dataset = track_dataset
    TrackerClass.track_sequence = track_sequence
    return TrackerClass(*params)


