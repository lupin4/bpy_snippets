import os
import re

import bpy


frame_current = bpy.context.scene.frame_current
frame_string = f'{frame_current:04}'

cbi = bpy.context.scene.camera.data.background_images[0]
image = cbi.image

filename = os.path.basename(image.filepath)
filedir = os.path.dirname(image.filepath)


match = re.match('(.*_)(\d+)(.png)', filename)
filename_components = list(match.groups())

filename_components[-2] = frame_string
filename_new = ''.join(filename_components)
filepath_new = os.path.join(filedir, filename_new)

if os.path.exists(filepath_new):
    cbi.image.filepath = filepath_new
