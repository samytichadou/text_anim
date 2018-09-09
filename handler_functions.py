import bpy

from .update_functions import update_char_spacing, update_char_position

#main update for handler
def handler_update_main():
    for ob in bpy.context.scene.objects:
        if len(ob.text_anim)!=0:
            controller=ob
            
            #do something
            update_char_spacing(controller)
            update_char_position(controller)