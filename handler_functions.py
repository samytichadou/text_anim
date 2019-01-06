import bpy

from .update_functions import *
from .misc_functions import get_list_from_controller, change_object_index
from .evaluation_functions import evaluation_linear_pct

#main update for handler
#copy of the main updater function without reset option
def handler_update_main():
    for ob in bpy.context.scene.objects:
        if len(ob.text_anim) != 0:
            controller = ob
            
            #get object list
            obj_list=get_list_from_controller(controller)
                
            #return anims from controller
            anim_list=[]
            try:
                for anim in controller.text_anim[0].animations:
                    if anim.active==True:
                        anim_list.append(anim)
            except IndexError:
                pass
            
            idx = 0
            for a in anim_list:
                if a.active :
                    print(a.name)
                    #get influences
                    inf_list=evaluation_linear_pct(a, controller)
                    
                    #do things
                    
                    # CREATE LISTS
                        # original values
                    if idx == 0 :
                        loc_list = []
                        scale_list = []
                        for obj in obj_list :
                            loc_list.append(obj.data.text_anim[0].original_location)
                            scale_list.append(obj.data.text_anim[0].original_scale)
                        # new values
                    else :
                        loc_list = get_loc_list(obj_list)
                        scale_list = get_scale_list(obj_list)

                    # LOCATION
                    if a.location_active :
                        update_char_position(a, controller, obj_list, inf_list, loc_list)
                        loc_list = get_loc_list(obj_list)

                    # SPACING
                    if a.spacing_active :
                        update_char_spacing(a, controller, obj_list, loc_list, inf_list)
                    
                    # DATA
                    if a.node_active :
                        update_data_value(a, controller, obj_list, inf_list)

                    # SCALE
                    if a.scale_active :
                        update_char_scale(a, controller, obj_list, inf_list, scale_list)
                        scale_list = get_scale_list(obj_list)

                    idx += 1