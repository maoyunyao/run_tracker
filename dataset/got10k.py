import numpy as np
import os
from .utils import Sequence

class GOT10KDataset:
    """ GOT-10k dataset.

        Publication:
            GOT-10k: A Large High-Diversity Benchmark for Generic Object Tracking in the Wild
            Lianghua Huang, Xin Zhao, and Kaiqi Huang
            arXiv:1810.11981, 2018
            https://arxiv.org/pdf/1810.11981.pdf

        Download dataset from http://got-10k.aitestunion.com/downloads
    """
    def __init__(self, dataset_path, split):
        """
        args:
            split - Split to use. Can be i) 'test': official test set, ii) 'val': official val set.
        """
        # Split can be test or val
        if split == 'test' or split == 'val':
            self.base_path = os.path.join(dataset_path, split)
        else:
            raise ValueError("Unrecognized split option")

        self.sequence_name_list = self._get_sequence_name_list(split)
        self.sequence_list = [self._construct_sequence(s) for s in self.sequence_name_list]

    def _construct_sequence(self, sequence_name):
        anno_path = '{}/{}/groundtruth.txt'.format(self.base_path, sequence_name)
        try:
            ground_truth_rect = np.loadtxt(str(anno_path), dtype=np.float64)
        except:
            ground_truth_rect = np.loadtxt(str(anno_path), delimiter=',', dtype=np.float64)

        frames_path = '{}/{}'.format(self.base_path, sequence_name)
        frame_list = [frame for frame in os.listdir(frames_path) if frame.endswith(".jpg")]
        frame_list.sort(key=lambda f: int(f[:-4]))
        frames_list = [os.path.join(frames_path, frame) for frame in frame_list]

        return Sequence(sequence_name, frames_list, ground_truth_rect.reshape(-1, 4))

    def _get_sequence_name_list(self):
        with open('{}/list.txt'.format(self.base_path)) as f:
            sequence_name_list = f.read().splitlines()
        return sequence_name_list
