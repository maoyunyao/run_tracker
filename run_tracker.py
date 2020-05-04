import os
import argparse
import importlib
import cv2 as cv
import numpy as np

from dataset import OTBDataset, LaSOTDataset, UAVDataset
from dataset import NFSDataset, TrackingNetDataset, TPLDataset
from dataset import VOTDataset, GOT10KDataset

from config import config

def run(tracker_name, dataset_name, output_dir):
    tracker_module = importlib.import_module('trackers.{}'.format(tracker_name))
    tracker = tracker_module.get_tracker()
    
    if dataset_name == 'otb':
        dataset = OTBDataset(config.otb_path)
    elif dataset_name == 'lasot':
        dataset = LaSOTDataset(config.lasot_path)
    elif dataset_name == 'uav':
        dataset = UAVDataset(config.uav_path)
    elif dataset_name == 'nfs':
        dataset = NFSDataset(config.nfs_path)
    elif dataset_name == 'trackingnet':
        dataset = TrackingNetDataset(config.trackingnet_path)
    elif dataset_name == 'tpl':
        dataset = TPLDataset(config.tpl_path, exclude_otb=False)
    elif dataset_name == 'VOT':
        dataset = VOTDataset(config.vot_path)
    elif dataset_name == 'got10k_test':
        dataset = GOT10KDataset(config.got10k_test_path, split='test')
    elif dataset_name == 'got10k_val':
        dataset == GOT10KDataset(config.got10k_val_path, split='val')
    else:
        raise ValueError("Unrecognized dataset name")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
    
    tracker.track_dataset(dataset, output_dir)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run tracker on dataset.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('dataset_name', type=str, help='Name of dataset to be tracked on.')
    parser.add_argument('output_dir', type=str, help='Path to save tracking result.')

    args = parser.parse_args()
    run(args.tracker_name, args.dataset_name, args.output_dir)