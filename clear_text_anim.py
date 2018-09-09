import bpy

from .misc_functions import delete_textanim_props

class ClearTextAnim(bpy.types.Operator):
    bl_idname = "textanim.clear_textanim"
    bl_label = "Clear"
    bl_description = ""
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='FONT':
                if len(act.data.text_anim)==1:
                    chk=1
        return chk==1

    def execute(self, context):
        text=context.active_object
        
        delete_textanim_props(text)
        
        return {"FINISHED"}
        