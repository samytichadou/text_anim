import bpy

from bpy.app.handlers import persistent

from .handler_functions import handler_update_main

@persistent
def text_anim_handler(scene):
    handler_update_main()