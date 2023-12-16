import os
from yacs.config import CfgNode

_C = CfgNode()

_C.DATASET_DIR = 'Car_Logo_Dataset_27'
_C.IMAGE_DIR = os.path.join(_C.DATASET_DIR, 'Car_Logo_Dataset_27_Images')
_C.ANNOT_FILE = os.path.join(
    _C.DATASET_DIR, 'Car Logo Dataset 27 Annotations DETR.txt')
_C.CROPPED_ANNOT_FILE = os.path.join(
    _C.DATASET_DIR, 'car_logos_27_dataset_training_set_annotation_cropped.txt')
_C.CROPPED_ANNOT_FILE_TEST = os.path.join(
    _C.DATASET_DIR, 'car_logos_27_dataset_test_set_annotation_cropped.txt')

_C.CLASS_NAMES = ['Audi', 'Citroen', 'GMC', 'Honda', 'Hyundai', 'Mazda', 'Mercedes', 'Mitsubishi', 
                  'Nissan', 'Renault', 'Toyota', 'Volkswagen', 'bmw', 'cadillac', 'chevrolet', 'ford', 'jeep', 
                  'kia', 'lexus', 'license-plate', 'mini', 'porsche', 'ram', 'range-rover', 'subaru', 'suzuki', 'volvo']


def get_cfg_defaults():
    return _C.clone()
