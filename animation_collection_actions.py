import bpy

# New animation
class TextAnimNewAnimation(bpy.types.Operator):
    bl_idname = "textanim.new_animation"
    bl_label = "New"
    bl_description = "Add New Animation"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='EMPTY':
                if len(act.text_anim)==1:
                    chk=1
        return chk==1

    def execute(self, context):
        controller=context.active_object
        props = controller.text_anim[0]
        
        #add
        prop=props.animations.add()
        
        return {"FINISHED"}
    
# Delete animation
class TextAnimDeletenimation(bpy.types.Operator):
    bl_idname = "textanim.delete_animation"
    bl_label = "Delete"
    bl_description = "Delete Animation"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='EMPTY':
                if len(act.text_anim)==1:
                    if len(act.text_anim[0].animations)!=0:
                        chk=1
        return chk==1
    
    indx = bpy.props.IntProperty()

    def execute(self, context):
        controller=context.active_object
        props = controller.text_anim[0]
        
        #add
        prop=props.animations.remove(self.indx)
        
        return {"FINISHED"}

# Change Animation Order
class TextAnimMoveAnimation(bpy.types.Operator):
    bl_idname = "textanim.move_animation"
    bl_label = "Move"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='EMPTY':
                if len(act.text_anim)==1:
                    if len(act.text_anim[0].animations)!=0:
                        chk=1
        return chk==1

    action = bpy.props.EnumProperty(
        items=(
            ('UP', "Up", ""),
            ('DOWN', "Down", ""),))
            
    indx = bpy.props.IntProperty()

    def invoke(self, context, event):
        scn = context.scene
        controller = context.active_object
        props = controller.text_anim[0]
        indx=self.indx
        items = props.animations

        if self.action == 'DOWN' and indx < len(items) - 1:
            oidx=indx
            items.move(indx, indx+1)
            
        elif self.action == 'UP' and indx >= 1:
            oidx=indx
            items.move(indx, indx-1)
            
        return {"FINISHED"}