import cv2
import numpy as np
from tqdm import tqdm

def track_dataset(self, dataset, output_dir):

    for seq in tqdm( dataset.sequence_list ):
        seq_result = self.track_sequence(seq)
        result_path = '{}/{}.txt'.format(output_dir, seq.name)
        np.savetxt(result_path, seq_result, delimiter='\t', fmt='%d')
    print("Done!")


def track_sequence(self, seq):
    '''
    init_bbox, bbox: [xmin, ymin, width, height], one-based
    '''
    seq_result = []
    
    init_info = seq.init_info()
    init_frame = init_info['init_frame']
    init_bbox = init_info['init_bbox']

    seq_result.append(init_bbox)
    
    frame_bgr = cv2.imread(init_frame)
    frame = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    self.init(frame, init_bbox)

    for i in range(1, seq.length):
        frame = seq.frames[i]
        frame_bgr = cv2.imread(frame)
        frame = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        bbox = self.track(frame)
        seq_result.append(bbox)
    
    return seq_result

    
    