bpy.data.images['Image'].filepath = filepath

bpy.ops.image.reload({'context': context,
                      'area': area}
                      )
