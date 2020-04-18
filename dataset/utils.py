class Sequence:
    """Class for a sequence."""
    def __init__(self, name, frames, ground_truth_rect):
        self.name = name
        self.frames = frames
        self.ground_truth_rect = ground_truth_rect
        self.length = len(frames)

    def init_info(self):
        return {key: self.get(key) for key in ['init_bbox', 'init_frame']}

    def init_bbox(self):
        return list(self.ground_truth_rect[0,:])
    
    def init_frame(self):
        return self.frames[0]

    def get(self, name):
        return getattr(self, name)()