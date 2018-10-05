import bpy

from .misc_functions import get_list_from_controller, change_object_index
from .evaluation_functions import evaluation_linear_pct

#update main
def update_fct_main(self, context):
    controller=context.active_object
    
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
        inf_list=evaluation_linear_pct(a)
        
    #do things
        loc_list=update_char_position(a, obj_list, inf_list)
        update_char_spacing(a, obj_list, loc_list, inf_list)
        update_data_value(a, obj_list, inf_list)
        update_char_scale(a, obj_list, inf_list)


### TODO ####
    # adapter fonctions update pour les différentes animations

##update function for char spacing
#def update_fct_char_spacing(self, context):
#    controller=context.active_object
#    update_char_spacing(controller)

#update char position
def update_char_position(animation, obj_list, inf_list):
    new_loc_list=[]
    
    for i in range(0, len(obj_list)):
        obj=obj_list[i]
        inf=inf_list[i]
        
        loc=obj.data.text_anim[0].original_location
        tarloc=animation.location
        
        newloc=(tarloc[0]*inf, tarloc[1]*inf, tarloc[2]*inf)
        
        x=loc[0]+newloc[0]
        y=loc[1]+newloc[1]
        z=loc[2]+newloc[2]
                
        obj.location=(x,y,z)
        
        new_loc_list.append((x,y,z))
        
    return new_loc_list
        
#update char spacing
def update_char_spacing(animation, obj_list, loc_list, inf_list):
    
    spacing=animation.spacing
    previous=obj_list[0].location[0]
    offset=0

    if animation.spacing_type=='LEFT':
        for i in range(0,len(obj_list)):
            inf=inf_list[i]
            obj=obj_list[i]
            
            previous=obj.location[0]
            #place chars
            obj.location[0]=loc_list[i][0]+((spacing*i-offset)*inf)+offset
            
            if animation.spacing_offset==True:
                offset=obj.location[0]-previous
            else:
                offset=0
    else:
        for i in range(len(obj_list)-1, -1, -1):
            inf=inf_list[i]
            obj=obj_list[i]
            
            previous=obj.location[0]
            #place chars
            obj.location[0]=loc_list[i][0]-((spacing*(len(obj_list)-1-i))*inf)-(offset-(offset*inf))
            
            if animation.spacing_offset==True:
                offset=previous-obj.location[0]
            else:
                offset=0

#update data value
def update_data_value(animation, obj_list, inf_list):
    min=animation.custom_node_data_base
    max=animation.custom_node_data_target
    
    for i in range(0,len(obj_list)):
        inf=inf_list[i]
        obj=obj_list[i]
        
        #map value
        value=min+(inf*max)
        change_object_index(value, obj)
        
#update char scale
def update_char_scale(animation, obj_list, inf_list):
    for i in range(0, len(obj_list)):
        obj=obj_list[i]
        inf=inf_list[i]
        
        scale=obj.data.text_anim[0].original_scale
        
        if animation.unified_scale_toggle==False:
            tarscale=animation.scale
        else:
            unif=animation.scale_unified
            tarscale=[unif,unif,unif]
        
        newscale=(tarscale[0]*inf, tarscale[1]*inf, tarscale[2]*inf)
        
        x=scale[0]*(1-inf)+newscale[0]
        y=scale[1]*(1-inf)+newscale[1]
        z=scale[2]*(1-inf)+newscale[2]
                
        obj.scale=(x,y,z)
        
        #add offset
        if animation.scale_offset==True:
            
            loc=obj.location
                        
            lx=loc[0]*x
            ly=loc[1]
            lz=loc[2]
            
            obj.location=(lx,ly,lz)
