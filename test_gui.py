import bpy

class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "textanim.test_gui"
    bl_label = "TextAnim"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    @classmethod
    def poll(cls, context):
        chk=0
        if context.active_object != None:
            act=context.active_object
            if act.type=='FONT':
                chk=1
            elif len(act.text_anim)!=0:
                chk=1
        return chk==1

    def draw(self, context):
        act = context.active_object
        
        layout = self.layout

        row = layout.row()
        
        #font menu
        if act.type=='FONT':
            row.operator('textanim.initialize_textanim')
            row.operator('textanim.clear_textanim')
            
            #debug
            row = layout.row()
            row.label(str(act.data.text_anim[0].index))
            row = layout.row()
            row.label(act.data.text_anim[0].controller)
                    
        else:
            row.prop(act.text_anim[0], 'start_pct', slider=True)
            row.prop(act.text_anim[0], 'end_pct', slider=True)
            row = layout.row()
            row.prop(act.text_anim[0], 'location', text="")
            row = layout.row()
            row.prop(act.text_anim[0], 'spacing')
            row.prop(act.text_anim[0], 'spacing_offset')
            row.prop(act.text_anim[0], 'spacing_type', text='')
            row = layout.row()
            row.prop(act.text_anim[0], 'custom_node_data_start')
            row.prop(act.text_anim[0], 'custom_node_data_end')