import re
import pathlib
import bpy


frame_current = bpy.context.scene.frame_current
frame_string = f'{frame_current:04}'

cbi = bpy.context.scene.camera.data.background_images[0]
image = cbi.image

filepath = pathlib.Path(image.filepath)

match = re.match('(.*_)(\d+)(.png)', filepath.name)
filename_components = list(match.groups())
filename_components[-2] = frame_string
filename_new = ''.join(filename_components)

filepath_new = filepath.parent.joinpath(filename_new)


if filepath_new.exists():
    image.filepath = str(filepath_new)
