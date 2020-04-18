# run_tracker
A  python toolkit for running your tracker on datasets: 
[OTB100](http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html), 
[LaSOT](https://cis.temple.edu/lasot/),
[UAV123](https://uav123.org/),
[NFS](http://ci2cv.net/nfs/index.html),
[Temple Color 128](http://www.dabi.temple.edu/~hbling/data/TColor-128/TColor-128.html),
[TrackingNet](https://tracking-net.org/),
[GOT-10k](http://got-10k.aitestunion.com/) and 
[VOT2018](http://www.votchallenge.net/vot2018/dataset.html)



## Usage

### Requirements

```
opencv-python
numpy
```
and other package required by your trackers



### Code modification

To run this toolkit on your working space, you will have to do a little modification on the code:

- Find the following code in ***config.py*** and replace them with your dataset path.

```python
###################################################################
# YOU NEED TO REPLACE THE FOLLOWING PATH WITH YOUR OWN DATASET PATH 
###################################################################

class Config:

    # Dataset path
    otb_path = '/data5/maoyy/dataset/OTB100'
    uav_path = '/data5/maoyy/dataset/UAV123'
    lasot_path = '/data5/maoyy/dataset/LaSOT'
    nfs_path = ''
    vot_path = '/data5/maoyy/dataset/VOT2018'
    trackingnet_path = ''
    tpl_path = ''
    got10k_path = '/data5/maoyy/dataset/GOT10k'


config = Config()
```

- Create python files for your tracker in ***trackers/*** , see ***example.py*** for inference. Here is an example:
```python
########################################################################
# YOU NEED TO IMPLEMENT THE FOLLOWING CODE SO THAT THIS TOOLKIT CAN HAVE 
# ACCESS TO YOUR TRACKER WITHOUT MOVING YOUR TRACKER TO THIS WORKSPACE
########################################################################
# Where your tracker is implemented:
tracker_path = '/data5/maoyy'
import sys
sys.path.append(tracker_path)
from SiamFC_crop import SiamFCCropTracker as TrackerClass

# Param(s) your tracker needed:
model_path = '/data5/maoyy/SiamFC_crop/models/siamfc_crop_30.pth'
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
```


### Run

After all configurations done, you are able to run the following command to run your tracker on datasets:

```python
python run_tracker.py tracker_name dataset_name output_path
```
For example:
```python
python run_tracker.py SiamFCCropTracker otb ./Result/OTB100/SiamFCCropTracker
```
Where tracker_name should be the same as the python file you implemented in ***trackers/*** folder.


