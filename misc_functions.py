import bpy

#delete textanim prop
def delete_textanim_props(object):
    prop=object.data.text_anim
    for i in range(len(prop)-1,-1,-1):
        prop.remove(i)
    return (object)

#split text, set controller and return list
def split_text_char(text, controller):
    body=text.data.body
    basename=text.name
    scn=bpy.context.scene
    obj_list=[]
    
    #deselect
    text.select=False
    
    idx=-1
    for c in list(body):
        idx+=1
        name=c
        
        #create
        obj = text.copy()
        obj.data = text.data.copy()
        obj.data.body=c
        obj.animation_data_clear()
        obj.name=name
        scn.objects.link(obj)
        
        #set idx
        prop=obj.data.text_anim[0]
        prop.index=idx
        prop.controller=str(controller)
                
        #append in list
        obj_list.append(obj)
        
    return obj_list

#place split texts and return list
def place_split_text(obj_list):
    newloc_x=0.000000
    for obj in obj_list:
        #place chars
        obj.location[0]=obj.data.text_anim[0].original_location[0]=newloc_x
                
        #update for object
        bpy.context.scene.update()
        
        #store bound
        newloc_x=obj.location[0]+obj.bound_box[4][0]
    return obj_list

#add prop to font object
def add_textanim_font_prop(obj):
    prop=obj.data.text_anim.add()
    prop.name="text_anim"
    return obj

#add prop to controller object
def add_textanim_controller_prop(obj):
    prop=obj.text_anim.add()
    prop.name="text_anim"
    return obj
    
#create empty controller at object position, parent it, and return controller
def create_controller(object):
    #get location
    loc=object.location
    rot=object.rotation_euler
    scale=object.scale
    
    #create controller
    name=object.data.body
    
    empty = bpy.data.objects.new( "empty", None )
    bpy.context.scene.objects.link(empty)
    
    #set empty
    empty.name=name
    empty.location=loc
    empty.rotation_euler=rot
    empty.scale=scale
    add_textanim_controller_prop(empty)
    
    #parent
    object.parent=empty
    
    #reset obj loc rot scale
    object.location=object.rotation_euler=[0,0,0]
    object.scale=[1,1,1]
    
    ###TODO### #parent controller to object's parent if there is one
    return empty

#get list from controller
def get_list_from_controller(controller):
    object_list=[]
    for obj in bpy.context.scene.objects:
        try:
            if len(obj.data.text_anim)!=0:
                if str(controller)==obj.data.text_anim[0].controller:
                    object_list.append(obj)
        except AttributeError:
            pass
    sorted_list = sorted(object_list, key=lambda x: x.data.text_anim[0].index, reverse=False)
    return sorted_list

#update object index
def change_object_index(value, object):
    object.pass_index = value*1000
