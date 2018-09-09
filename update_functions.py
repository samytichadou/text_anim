import bpy

from .misc_functions import get_list_from_controller
from .evaluation_functions import evaluation_linear_pct

#update main
def update_fct_main(self, context):
    controller=context.active_object
    
    #get influences
    inf_list=evaluation_linear_pct(controller)
    
    #do things
    loc_list=update_char_position(controller, inf_list)
    update_char_spacing(controller, loc_list, inf_list)

#update function for char spacing
def update_fct_char_spacing(self, context):
    controller=context.active_object
    update_char_spacing(controller)

#update char position
def update_char_position(controller, inf_list):
    new_loc_list=[]
    
    obj_list=get_list_from_controller(controller)
    
    for i in range(0, len(obj_list)):
        obj=obj_list[i]
        inf=inf_list[i]
        
        loc=obj.data.text_anim[0].original_location
        tarloc=controller.text_anim[0].location
        
        newloc=(tarloc[0]*inf, tarloc[1]*inf, tarloc[2]*inf)
        
        x=loc[0]+newloc[0]
        y=loc[1]+newloc[1]
        z=loc[2]+newloc[2]
                
        obj.location=(x,y,z)
        
        new_loc_list.append((x,y,z))
        
    return new_loc_list
        
#update char spacing
def update_char_spacing(controller, loc_list, inf_list):
    
    bpy.context.scene.update()
    
    obj_list=get_list_from_controller(controller)
    
    spacing=controller.text_anim[0].spacing
    previous=obj_list[0].location[0]
    offset=0
    previous=0
    if controller.text_anim[0].spacing_type=='LEFT':
        for i in range(0,len(obj_list)):
            inf=inf_list[i]
            obj=obj_list[i]
            
            previous=obj.location[0]
            
            #place chars
            obj.location[0]=loc_list[i][0]+((spacing*i-offset)*inf)+offset
            
            if controller.text_anim[0].spacing_offset==True:
                offset=obj.location[0]-previous
            else:
                offset=0
    else:
        for i in range(len(obj_list)-1, -1, -1):
            inf=inf_list[i]
            obj=obj_list[i]
            
            previous=obj.location[0]
            
            #place chars
            obj.location[0]=loc_list[i][0]-((spacing*(len(obj_list)-1-i)-offset)*inf)+offset
            
            if controller.text_anim[0].spacing_offset==True:
                offset=obj.location[0]-previous
            else:
                offset=0
            