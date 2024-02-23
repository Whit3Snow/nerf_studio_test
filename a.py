import json
import numpy as np
from pathlib import Path
import argparse

import pdb 
def ind(c2w):
    if len(c2w) == 3:
        c2w += [[0, 0, 0, 1]]
    return c2w

parser = argparse.ArgumentParser("'")
parser.add_argument("--scene", type=str, required=True)
args = parser.parse_args()   

scene = args.scene
train_transforms = json.loads(open('poses/transforms_train.json'.format(scene)).read())
# eval_transforms = json.loads(open('poses/transforms_eval.json').read())
# transforms = train_transforms + eval_transforms
transforms = train_transforms

transforms = sorted(transforms, key=lambda x: Path(x['file_path']).stem)

out = {
        'camera_type': 'perspective',
        'render_height': 567,
        'render_width': 1008,
        'seconds': len(transforms),
        'camera_path': [
            {'camera_to_world': ind(pose['transform']), 'fov':40, 'aspect': 1, 'file_path': pose['file_path']}
            for pose in transforms
            ]
        }

outstr = json.dumps(out, indent=4)
print(outstr)
with open('camera_path_{}.json'.format(scene), mode='w') as f:
    print("running")
    f.write(outstr)
    print()