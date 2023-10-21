import bpy

import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob)


class SetViewportDisplayToCollection(bpy.types.Operator):
    bl_idname = "object.viewport_display_to_collection"
    bl_label = "Set Viewport Display parameters to Collection"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SetViewportDisplayToCollection)


def unregister():
    bpy.utils.unregister_class(SetViewportDisplayToCollection)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()