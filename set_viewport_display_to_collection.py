import bpy
import random

class SetViewportDisplayToCollection(bpy.types.Operator):
    bl_idname = "object.viewport_display_to_collection"
    bl_label = "Display Color Collection"
    bl_options = {'REGISTER', 'UNDO'}

    # Create properties.
    color: bpy.props.FloatVectorProperty(
        name = "Colour",
        description = "Viewport display color set to all direct children objects of the currently selected objects collection.",
        subtype = "COLOR",
        size=4,
        default=(0.5, 0.5, 0.5, 1)
    )

    def execute(self, context):
        collection = context.object.users_collection

        for obj in collection[0].objects:
            obj.color = self.color

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SetViewportDisplayToCollection)


def unregister():
    bpy.utils.unregister_class(SetViewportDisplayToCollection)


if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.object.simple_operator()