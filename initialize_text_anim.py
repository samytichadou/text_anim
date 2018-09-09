import bpy

from .misc_functions import add_textanim_font_prop, create_controller, split_text_char, place_split_text

class InitializeTextAnim(bpy.types.Operator):
    bl_idname = "textanim.initialize_textanim"
    bl_label = "Initialize"
    bl_description = ""
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='FONT':
                if len(act.data.text_anim)==0:
                    chk=1
        return chk==1

    def execute(self, context):
        text=context.active_object
        body=text.data.body

        #add prop
        add_textanim_font_prop(text)
        
        #create controller and parent object
        control=create_controller(text)
        
        #split text and place it
        obj_list=split_text_char(text, control)
        place_split_text(obj_list)
        
        #delete base object
        bpy.data.objects.remove(bpy.data.objects[text.name], True)
        
        #select controller
        context.scene.objects.active=control
        control.select=True
        
        return {"FINISHED"}        