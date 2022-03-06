import bpy

asset_name = "Road_Endcap"

bpy.ops.object.select_linked()

context = bpy.context

view_layer = context.view_layer
layer_collection = view_layer.layer_collection

ao = context.active_object
sos = context.selected_objects


prototypes = view_layer.layer_collection.children['Prototypes']

prototype = bpy.data.collections.new(f"{asset_name}")
prototypes.collection.children.link(prototype)
view_layer.active_layer_collection = prototypes.children[f"{asset_name}"]
view_layer.active_layer_collection.exclude = True

instances = bpy.data.collections.new(f"{asset_name}_Instances")
prototypes.collection.children.link(instances)


proto = bpy.data.objects.new(asset_name, ao.data)
proto.scale = ao.parent.matrix_world.to_scale()

layer_collection.children['Prototypes'].collection.children[asset_name].objects.link(proto)

instances = prototypes.children[f"{asset_name}_Instances"]
view_layer.active_layer_collection = instances

for index, o in enumerate(sos, 1):
    bpy.ops.object.empty_add()

    locator = bpy.context.active_object

    locator.name = f"{asset_name}_{index:003}"

    try:
        instances.collection.objects.link(locator)
    except RuntimeError as rte:
        print(rte)

    locator.instance_type = 'COLLECTION'
    locator.instance_collection = prototypes.collection.children[asset_name]

    locator.matrix_world = o.matrix_world
    locator.scale = o.scale
