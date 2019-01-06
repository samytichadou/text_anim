import bpy

class TextAnimTestGUI(bpy.types.Panel):
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
            #animations
            row = layout.row()
            row.operator('textanim.new_animation')
            try:
                idx=-1
                for i in act.text_anim[0].animations:
                    idx+=1
                    box=layout.box()
                    
                    # HEADER
                                        
                    row=box.row(align=True)
                    if i.hidden==True:
                        row.prop(i, 'hidden', text='', icon='TRIA_RIGHT', emboss=False)
                    else:
                        row.prop(i, 'hidden', text='', icon='TRIA_DOWN', emboss=False)
                    if i.active==True:
                        row.prop(i, 'active', icon='VISIBLE_IPO_ON', text="", emboss=False)
                    else:
                        row.prop(i, 'active', icon='VISIBLE_IPO_OFF', text="", emboss=False)
                    row.prop(i, 'name', text='')
                    op = row.operator('textanim.move_animation', icon='TRIA_UP', text="")
                    op.action='UP'
                    op.indx=idx
                    op = row.operator('textanim.move_animation', icon='TRIA_DOWN', text="")
                    op.action='DOWN'
                    op.indx=idx
                    row.operator('textanim.delete_animation', icon='PANEL_CLOSE', text="").indx=idx
                    
                    # Animation details
                    
                    if i.hidden==False:
                        
                        row = box.row(align=True)
                        row.prop(i, 'start_pct', slider=True)
                        row.prop(i, 'end_pct', slider=True)

                        row=box.row(align=True)
                        row.prop(i, 'overlap_value', slider = True)
                        row.prop(i, 'smooth_in')
                        row.prop(i, 'smooth_out')
                        row.separator()
                        row.prop(i, 'location_active', text='', icon='MAN_TRANS')
                        row.prop(i, 'scale_active', text='', icon='MAN_SCALE')
                        row.prop(i, 'spacing_active', text='', icon='ARROW_LEFTRIGHT')
                        row.prop(i, 'node_active', text='', icon='NODETREE')
                        
                        col=box.column(align=True)
                        
                        if i.location_active :
                            box2=col.box()
                            row = box2.row(align=True)
                            row.label(icon='MAN_TRANS')
                            row.separator()
                            row.prop(i, 'location', text="")

                        if i.scale_active :        
                            box2=col.box()
                            row = box2.row(align=True)
                            row.label(icon='MAN_SCALE')
                            row.separator()
                            row.prop(i, 'scale_offset', text='', icon='NOCURVE')
                            row.separator()
                            if i.unified_scale_toggle==True:
                                row.prop(i, 'scale_unified', text='')
                            else:
                                row.prop(i, 'scale', text='')
                            row.prop(i, 'unified_scale_toggle', text='', icon='MANIPUL')
                        
                        if i.spacing_active :
                            box2=col.box()
                            row = box2.row(align=True)
                            row.label(icon='ARROW_LEFTRIGHT')
                            row.separator()
                            row.prop(i, 'spacing_offset', text='', icon='NOCURVE')
                            row.prop(i, 'spacing_type', text='')
                            row.prop(i, 'spacing', text='')

                        if i.node_active :
                            box2=col.box()
                            row = box2.row(align=True)
                            row.label(icon='NODETREE')
                            row.separator()
                            row.prop(i, 'custom_node_data_base', text='Base')
                            row.prop(i, 'custom_node_data_target', text='Target')
                        
                                                
            except IndexError:
                pass