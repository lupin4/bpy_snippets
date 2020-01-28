import bpy

context = bpy.context

view_layer = context.view_layer

view_layer.objects.active.select_set(False, view_layer=view_layer)

view_layer.objects.active = bpy.data.objects['Camera']
view_layer.objects.active.select_set(True, view_layer=view_layer)
