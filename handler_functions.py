import bpy

from .update_functions import update_char_position, update_char_spacing, update_data_value, update_char_scale
from .misc_functions import get_list_from_controller, change_object_index
from .evaluation_functions import evaluation_linear_pct

#main update for handler
def handler_update_main():
    for ob in bpy.context.scene.objects:
        if len(ob.text_anim)!=0:
            controller=ob
            
            #get object list
            obj_list=get_list_from_controller(controller)
            
            #return anims from controller
            anim_list=[]
            try:
                for anim in controller.text_anim[0].animations:
                    anim_list.append(anim)
            except IndexError:
                break
            
            for a in anim_list:

            #get influences
                inf_list=evaluation_linear_pct(a, obj_list)
                
            #do things
                loc_list=update_char_position(a, obj_list, inf_list)
                update_char_spacing(a, obj_list, loc_list, inf_list)
                update_data_value(a, obj_list, inf_list)
                update_char_scale(a, obj_list, inf_list)
