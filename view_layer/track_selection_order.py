import bpy


class SelectionCallback:
    def __init__(self):
        self.selection_order = []
    
    @staticmethod
    def notify(*args):
        self = args[0]
        layer_objects = bpy.context.view_layer.objects

        if not layer_objects:
            return

        print("\n\n")
        print(layer_objects.active)

        if not layer_objects.active in self.selection_order:
            self.selection_order.append(layer_objects.active)

        if len(layer_objects.selected) > 1:
            selected = set(bpy.context.view_layer.objects.selected)
            selected.remove(bpy.context.view_layer.objects.active)

            for o in selected:
                if not o in self.selection_order:
                    self.selection_order.append(o)

            removed = set(self.selection_order) - selected

            for r in removed:
                self.selection_order.remove(r)

            print(self.selection_order)
        else:
            self.selection_order = []


subscribe_to = bpy.types.LayerObjects, "active"

handle = SelectionCallback()

bpy.msgbus.subscribe_rna(
    key = subscribe_to,
    owner = handle,
    args = (handle,),
    notify = handle.notify,
    )
