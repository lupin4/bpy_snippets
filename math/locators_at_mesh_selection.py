import bpy
import mathutils

active_object = bpy.context.active_object

bpy.ops.object.mode_set(mode='OBJECT')

print('--------')

wmtx = mathutils.Matrix(active_object.matrix_world)
print(wmtx)

for polygon in active_object.data.polygons:
    if polygon.select:
        print(wmtx@polygon.normal, wmtx@polygon.center)
        bpy.ops.object.add(type='EMPTY',location=wmtx@polygon.center)
