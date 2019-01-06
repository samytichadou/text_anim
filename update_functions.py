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
            if anim.active==True:
                anim_list.append(anim)
    except IndexError:
        pass

    if len(anim_list)==0 :        
        #reset
        update_char_reset(controller, obj_list)
    
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

#get loc list
def get_loc_list(obj_list):
    loc_list = []
    for obj in obj_list :
        loc_list.append(obj.location)
    return loc_list

#get scale list
def get_scale_list(obj_list):
    scale_list = []
    for obj in obj_list :
        scale_list.append(obj.scale)
    return scale_list

#update char position
def update_char_position(animation, controller, obj_list, inf_list, loc_list):

    for i in range(0, len(obj_list)):
        obj=obj_list[i]
        inf=inf_list[i]
        
        #loc=obj.data.text_anim[0].original_location
        loc = loc_list[i]
        #tarloc=controller.text_anim[0].location
        tarloc=animation.location
        newloc=(tarloc[0]*inf, tarloc[1]*inf, tarloc[2]*inf)
        
        x=loc[0]+newloc[0]
        y=loc[1]+newloc[1]
        z=loc[2]+newloc[2]
               
        obj.location=(x,y,z)
        
#update char spacing
def update_char_spacing(animation, controller, obj_list, loc_list, inf_list):
    
    #spacing=controller.text_anim[0].spacing
    spacing=animation.spacing
    previous=obj_list[0].location[0]
    offset=0

    #if controller.text_anim[0].spacing_type=='LEFT':
    if animation.spacing_type=='LEFT':
        for i in range(0,len(obj_list)):
            inf=inf_list[i]
            obj=obj_list[i]
            
            previous=obj.location[0]
            #place chars
            obj.location[0]=loc_list[i][0]+((spacing*i-offset)*inf)+offset
            
            #if controller.text_anim[0].spacing_offset==True:
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
            
            #if controller.text_anim[0].spacing_offset==True:
            if animation.spacing_offset==True:
                offset=previous-obj.location[0]
            else:
                offset=0

#update data value
def update_data_value(animation, controller, obj_list, inf_list):
    props=controller.text_anim[0]
    #min=props.custom_node_data_base
    #max=props.custom_node_data_target
    min=animation.custom_node_data_base
    max=animation.custom_node_data_target
    
    for i in range(0,len(obj_list)):
        inf=inf_list[i]
        obj=obj_list[i]
        
        #map value
        value=min+(inf*max)
        change_object_index(value, obj)
        
#update char scale
def update_char_scale(animation, controller, obj_list, inf_list, scale_list):
    for i in range(0, len(obj_list)):
        obj = obj_list[i]
        inf = inf_list[i]
        
        scale = scale_list[i]
        
        #if controller.text_anim[0].unified_scale_toggle==False:
        if animation.unified_scale_toggle == False :
            #tarscale=controller.text_anim[0].scale
            tarscale = animation.scale
        else:
            #unif=controller.text_anim[0].scale_unified
            unif = animation.scale_unified
            tarscale = [unif,unif,unif]
        
        newscale = ((tarscale[0] - 1) * inf, (tarscale[1] - 1) * inf, (tarscale[2] - 1) * inf)
        
        #x = scale[0]*(1-inf)+newscale[0]
        #y = scale[1]*(1-inf)+newscale[1]
        #z = scale[2]*(1-inf)+newscale[2]
        x = scale[0] * (newscale[0] + 1)
        y = scale[1] * (newscale[1] + 1)
        z = scale[2] * (newscale[2] + 1)

        obj.scale = (x,y,z)
        
        #add offset
        #if controller.text_anim[0].scale_offset==True:
        if animation.scale_offset == True :
            
            loc = obj.location
                        
            lx = loc[0] * (newscale[0] + 1)
            ly = loc[1]
            lz = loc[2]
            
            obj.location = (lx,ly,lz)

#reset
def update_char_reset(controller, obj_list):
    for obj in obj_list:
        #loc
        obj.location = obj.data.text_anim[0].original_location
        #scale
        obj.scale = obj.data.text_anim[0].original_scale
        #obj pass
        obj.pass_index = obj.data.text_anim[0].original_pass_index